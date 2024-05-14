from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import os

import requests
from dotenv import load_dotenv
import uvicorn

from src.utils import StatiFilesNoCache

load_dotenv()
MICROCMS_API_KEY=os.environ.get("MICROCMS_API_KEY")

if not MICROCMS_API_KEY:
    print("このアプリの動作には、環境変数にMICROCMS_API_KEYが必要です")
    raise Exception("Require MICROCMS_API_KEY")

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index_page(request: Request):
    context={}
    return templates.TemplateResponse(
        request=request, name="index.html", context=context
    )

@app.get("/words/{word}", response_class=HTMLResponse)
async def word_page(request: Request, word: str):
    res = requests.get(f'https://animal-dictionary.microcms.io/api/v1/words?filters=word[equals]{word}', headers={
        "X-MICROCMS-API-KEY": MICROCMS_API_KEY
    }, timeout=60).json()
    if len(res["contents"]) <= 0:
        return HTMLResponse("お探しの単語は見つかりませんでした", status_code=404)
    return templates.TemplateResponse(
        request=request, name="word.html", context={"word": word,"description": res["contents"][0]["description"]}
    )

@app.get("/api/search")
def search_api(word: str):
    res = requests.get(f'https://animal-dictionary.microcms.io/api/v1/words?filters=word[contains]{word}', headers={
        "X-MICROCMS-API-KEY": MICROCMS_API_KEY
    }, timeout=60).json()
    return res["contents"]

# 静的ファイルを設定
app.mount("/img-data", StatiFilesNoCache(directory="img-data",html=True), name="static")
app.mount("/", StatiFilesNoCache(directory="static",html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)