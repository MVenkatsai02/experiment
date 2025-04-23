import os
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# Load keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def search_articles(query):
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": SERPER_API_KEY}
    data = {"q": query}

    res = requests.post(url, headers=headers, json=data)
    results = res.json().get("organic", [])

    articles = []
    for r in results[:5]:
        article_url = r.get("link")
        if article_url:
            content = fetch_article_content(article_url)
            articles.append({
                "url": article_url,
                "title": r.get("title"),
                "content": content
            })

    return articles

def fetch_article_content(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.content, "html.parser")
        paragraphs = soup.find_all(["p", "h1", "h2", "h3"])
        content = "\n".join(p.get_text() for p in paragraphs if p.get_text())
        return content
    except Exception as e:
        return f"Error fetching content: {e}"

def concatenate_content(articles):
    combined = ""
    for article in articles:
        combined += f"Title: {article['title']}\n"
        combined += f"URL: {article['url']}\n"
        combined += f"{article['content']}\n\n"
    return combined.strip()

def generate_answer(content, query):
    model = genai.GenerativeModel("models/gemini-1.5-flash")

    prompt = f"""You are a helpful assistant. Based on the following content, answer the user's query.

Content:
{content}

Query:
{query}

Answer:"""

    response = model.generate_content(prompt)
    return response.text.strip()
