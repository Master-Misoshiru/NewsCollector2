import feedparser

SOURCES = [
    # デザイン系
    {"name": "Dezeen",          "url": "https://www.dezeen.com/feed/"},
    {"name": "It's Nice That",  "url": "https://www.itsnicethat.com/rss"},
    {"name": "Design Week",     "url": "https://www.designweek.co.uk/feed/"},
    {"name": "Creative Review", "url": "https://www.creativereview.co.uk/feed/"},
    {"name": "Wallpaper*",      "url": "https://www.wallpaper.com/rss"},
    {"name": "Design Taxi",     "url": "https://designtaxi.com/feed/news/"},
    # 広告・マーケティング系
    {"name": "Ad Age",          "url": "https://adage.com/rss/news"},
    {"name": "Adweek",          "url": "https://www.adweek.com/feed/"},
    {"name": "The Drum",        "url": "https://www.thedrum.com/rss.xml"},
    {"name": "Campaign",        "url": "https://www.campaignlive.co.uk/rss"},
    {"name": "Little Black Book","url": "https://lbbonline.com/feed"},
    # 日本語メディア
    {"name": "MdN Design",      "url": "https://www.mdn.co.jp/feed"},
    {"name": "AdverTimes",      "url": "https://www.advertimes.com/feed/"},
]


def fetch_articles():
    articles = []
    for source in SOURCES:
        try:
            feed = feedparser.parse(source["url"])
            for entry in feed.entries:
                url = entry.get("link", "")
                if not url:
                    continue
                articles.append({
                    "source": source["name"],
                    "title": entry.get("title", "(タイトルなし)"),
                    "url": url,
                    "summary": entry.get("summary", ""),
                })
        except Exception:
            pass
    return articles
