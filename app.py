import os
import time
from dotenv import load_dotenv
from sqlalchemy.orm import Session

from db import SessionLocal, SocialPost
from scraper import TwitterScraper, InstagramScraper

load_dotenv()


def save_posts(rows):
    db: Session = SessionLocal()
    try:
        for row in rows:
            if not row.get("post_url"):
                continue

            existing = db.query(SocialPost).filter(SocialPost.post_url == row["post_url"]).first()
            if existing:
                continue

            item = SocialPost(
                platform=row.get("platform", ""),
                username=row.get("username", ""),
                full_name=row.get("full_name", ""),
                profile_url=row.get("profile_url", ""),
                bio=row.get("bio", ""),
                followers=row.get("followers", 0),
                following=row.get("following", 0),
                posts_count=row.get("posts_count", 0),
                caption=row.get("caption", ""),
                media_url=row.get("media_url", ""),
                post_url=row.get("post_url", ""),
                hashtags=row.get("hashtags", ""),
                scraped_at=row.get("scraped_at"),
            )
            db.add(item)

        db.commit()
        print(f"Saved {len(rows)} posts")
    finally:
        db.close()


def main():
    twitter_keywords = [
        item.strip() for item in os.getenv("TWITTER_KEYWORDS", "Nigeria,Lagos,Abuja,Naija").split(",") if item.strip()
    ]
    instagram_handles = [
        item.strip() for item in os.getenv("INSTAGRAM_HANDLES", "naijagist,lagosstateofficial").split(",") if item.strip()
    ]
    request_delay = int(os.getenv("REQUEST_DELAY", "4"))

    twitter = TwitterScraper(twitter_keywords, request_delay=request_delay)
    instagram = InstagramScraper(instagram_handles, request_delay=request_delay)

    all_rows = []

    for keyword in twitter_keywords:
        print(f"Scraping Twitter keyword: {keyword}")
        all_rows.extend(twitter.scrape_keyword(keyword))
        time.sleep(request_delay)

    for handle in instagram_handles:
        print(f"Scraping Instagram handle: {handle}")
        all_rows.extend(instagram.scrape_handle(handle))
        time.sleep(request_delay)

    save_posts(all_rows)
    print("Finished scraping.")


if __name__ == "__main__":
    main()
