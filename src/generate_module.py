import os

import openai
import requests
from dotenv import load_dotenv

API_ENDPOINT = "https://zenn.dev/api/articles?&order=liked_count"
KEYWORDS = ["AI", "python", "chatgpt", "llm", "chat"]

load_dotenv(verbose=True)
openai.api_key = os.environ.get("OPENAI_API_KEY")


def get_popular_article(top_n: int = 10) -> list[dict[str, str]]:
    response_articles = requests.get(API_ENDPOINT).json()["articles"]
    popular_artilces = sorted(
        response_articles, key=lambda x: x["liked_count"], reverse=True
    )[:top_n]

    return popular_artilces


def choose_ai_article(popular_artilce: list[dict[str, str]]) -> list[dict[str, str]]:
    return popular_artilce[0]


def summary_tweet(ai_article: list[dict[str, str]]) -> str:
    personality = f"""
    あなたはAIやデータ活用のプロです。
    次の記事タイトルに対して、プロの観点から、活用方法や学びをシェアします。
    返答は140字以内で構成してください。
    回答フォーマットは以下です。

    【回答フォーマット】
    🎉注目記事を紹介🎉
    xxを学べる良い記事です!

    xxxのような人におすすめな記事かと!

    ・キーワード
    xxx, xxx, xxx

    https://zenn.dev/neet/articles/{ai_article["slug"]}
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": personality},
            {"role": "user", "content": ai_article["title"]},
        ],
    )
    return response["choices"][0]["message"]["content"]
