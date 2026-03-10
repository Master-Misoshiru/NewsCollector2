import os
import re

import google.generativeai as genai

_HTML_TAG_RE = re.compile(r"<[^>]+>")

_MODEL_NAME = "gemini-1.5-flash"

_PROMPT_TEMPLATE = """\
以下のニュース記事を日本語で2〜3文に要約してください。

タイトル: {title}
内容: {content}

日本語要約:"""


def summarize_in_japanese(title: str, content: str) -> str:
    api_key = os.environ.get("GOOGLE_API_KEY", "")
    if not api_key:
        return content

    plain_content = _HTML_TAG_RE.sub("", content).strip()
    if not plain_content:
        return content

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(_MODEL_NAME)
        prompt = _PROMPT_TEMPLATE.format(title=title, content=plain_content[:1000])
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception:
        return content
