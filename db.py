from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = os.getenv("DB_PATH", str(BASE_DIR / "data" / "nigeria_social.db"))
Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)

Base = declarative_base()

class SocialPost(Base):
    __tablename__ = "social_posts"

    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String, index=True)
    username = Column(String, index=True)
    full_name = Column(String, nullable=True)
    profile_url = Column(String, nullable=True)
    bio = Column(Text, nullable=True)
    followers = Column(Integer, default=0)
    following = Column(Integer, default=0)
    posts_count = Column(Integer, default=0)
    caption = Column(Text, nullable=True)
    media_url = Column(String, nullable=True)
    post_url = Column(String, unique=True, index=True)
    hashtags = Column(Text, nullable=True)
    scraped_at = Column(DateTime, default=datetime.utcnow)

engine = create_engine(f"sqlite:///{DB_PATH}")
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
