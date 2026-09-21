import re
import time
from datetime import datetime
from urllib.parse import quote

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


def clean_text(value):
    if not value:
        return ""
    return re.sub(r"\s+", " ", value).strip()


def extract_hashtags(text):
    if not text:
        return ""
    return ",".join(re.findall(r"#\w+", text))


class TwitterScraper:
    def __init__(self, keywords, request_delay=4):
        self.keywords = keywords
        self.request_delay = request_delay

    def build_search_url(self, keyword):
        return f"https://x.com/search?q={quote(keyword)}&src=typed_query"

    def extract_post(self, article):
        try:
            text = article.locator("div[data-testid='tweetText']").first.inner_text(timeout=2000)
        except Exception:
            text = ""

        text = clean_text(text)
        if not text:
            return None

        try:
            href = article.locator("a[href*='/status/']").first.get_attribute("href")
            url = f"https://x.com{href}" if href and not href.startswith("http") else href or ""
        except Exception:
            url = ""

        try:
            username = article.locator("a[href*='/']").nth(1).get_attribute("href")
            username = username.strip("/") if username else ""
            if username and not username.startswith("@"):
                username = f"@{username}"
        except Exception:
            username = ""

        return {
            "platform": "x",
            "username": username,
            "full_name": "",
            "profile_url": f"https://x.com/{username.replace('@', '')}" if username else "",
            "bio": "",
            "followers": 0,
            "following": 0,
            "posts_count": 0,
            "caption": text,
            "media_url": "",
            "post_url": url,
            "hashtags": extract_hashtags(text),
            "scraped_at": datetime.utcnow(),
        }

    def scrape_keyword(self, keyword):
        url = self.build_search_url(keyword)
        results = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(
                viewport={"width": 1500, "height": 1200},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            )
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(5000)

            for _ in range(2):
                page.mouse.wheel(0, 3000)
                page.wait_for_timeout(2000)

            for article in page.locator("article").all():
                try:
                    item = self.extract_post(article)
                    if item and item["caption"]:
                        results.append(item)
                except Exception:
                    continue

            browser.close()

        return results


class InstagramScraper:
    def __init__(self, handles, request_delay=4):
        self.handles = handles
        self.request_delay = request_delay

    def fetch_page(self, username):
        url = f"https://www.instagram.com/{username}/"
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(
                viewport={"width": 1500, "height": 1200},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            )
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            time.sleep(3)
            html = page.content()
            browser.close()
        return html

    def parse_number(self, value):
        if not value:
            return 0
        value = value.lower().replace(",", "")
        value = value.replace("k", "000").replace("m", "000000")
        try:
            return int(float(value))
        except ValueError:
            return 0

    def parse_profile(self, html, username):
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(" ", strip=True)

        followers = 0
        following = 0
        posts_count = 0

        match = re.search(r"(\d[\d,\.kKmM]*)\s*Followers", text)
        if match:
            followers = self.parse_number(match.group(1))

        match = re.search(r"(\d[\d,\.kKmM]*)\s*Following", text)
        if match:
            following = self.parse_number(match.group(1))

        match = re.search(r"(\d[\d,\.kKmM]*)\s*Posts", text)
        if match:
            posts_count = self.parse_number(match.group(1))

        bio = ""
        meta_desc = soup.select_one("meta[name='description']")
        if meta_desc:
            bio = clean_text(meta_desc.get("content", ""))

        recent_posts = []
        for a_tag in soup.select("a[href*='/p/']"):
            href = a_tag.get("href", "")
            if "/p/" not in href:
                continue
            post_url = f"https://www.instagram.com{href}" if not href.startswith("http") else href
            caption = clean_text(a_tag.get_text(" ", strip=True))
            recent_posts.append({
                "platform": "instagram",
                "username": username,
                "full_name": "",
                "profile_url": f"https://www.instagram.com/{username}/",
                "bio": bio,
                "followers": followers,
                "following": following,
                "posts_count": posts_count,
                "caption": caption,
                "media_url": "",
                "post_url": post_url,
                "hashtags": extract_hashtags(caption),
                "scraped_at": datetime.utcnow(),
            })

        return recent_posts[:5]

    def scrape_handle(self, username):
        time.sleep(self.request_delay)
        html = self.fetch_page(username)
        return self.parse_profile(html, username)
