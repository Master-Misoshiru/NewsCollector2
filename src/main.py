import json
import os
import sys
import time
from pathlib import Path

from collectors.rss_collector import fetch_articles
from notifiers.discord import post_article
from summarizer.gemini_summarizer import summarize_in_japanese

POSTED_FILE = Path(__file__).parent.parent / "data" / "posted.json"


def load_posted() -> set:
    if POSTED_FILE.exists():
        return set(json.loads(POSTED_FILE.read_text(encoding="utf-8")))
    return set()


def save_posted(posted: set) -> None:
    POSTED_FILE.parent.mkdir(exist_ok=True)
    POSTED_FILE.write_text(
        json.dumps(sorted(posted), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def main() -> None:
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL", "")
    if not webhook_url:
        print("ERROR: DISCORD_WEBHOOK_URL が設定されていません", file=sys.stderr)
        sys.exit(1)

    posted = load_posted()
    articles = fetch_articles()

    new_articles = [a for a in articles if a["url"] not in posted]
    print(f"取得記事数: {len(articles)}  未投稿: {len(new_articles)}")

    for article in new_articles:
        article["summary_ja"] = summarize_in_japanese(
            article["title"], article.get("summary", "")
        )
        success = post_article(webhook_url, article)
        if success:
            posted.add(article["url"])
            print(f"  投稿: [{article['source']}] {article['title']}")
        else:
            print(f"  失敗: [{article['source']}] {article['title']}", file=sys.stderr)
        time.sleep(1)  # Discord レート制限対策

    save_posted(posted)
    print("完了")


if __name__ == "__main__":
    main()
