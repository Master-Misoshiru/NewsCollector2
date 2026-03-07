import re
import time
import requests

# Discord embed の色（ブランドカラー）
EMBED_COLOR = 0x5865F2

_HTML_TAG_RE = re.compile(r"<[^>]+>")


def _strip_html(text: str) -> str:
    return _HTML_TAG_RE.sub("", text).strip()


def post_article(webhook_url: str, article: dict) -> bool:
    summary = _strip_html(article.get("summary", ""))
    if len(summary) > 200:
        summary = summary[:197] + "..."

    payload = {
        "embeds": [
            {
                "title": article["title"],
                "url": article["url"],
                "description": summary,
                "footer": {"text": article["source"]},
                "color": EMBED_COLOR,
            }
        ]
    }

    for attempt in range(3):
        response = requests.post(webhook_url, json=payload, timeout=10)
        if response.status_code == 204:
            return True
        if response.status_code == 429:
            retry_after = response.json().get("retry_after", 1)
            time.sleep(retry_after)
            continue
        break

    return False
