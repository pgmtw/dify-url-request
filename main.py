from fastapi import FastAPI, Query
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/fetch-url")
def fetch_url(url: str):
    try:
        resp = requests.get(url, timeout=5)
        soup = BeautifulSoup(resp.text, "html.parser")
        text = soup.get_text()
        return {"text": text[:3000]}  # 限制最大字數以避免 token 爆掉
    except Exception as e:
        return {"error": str(e)}
