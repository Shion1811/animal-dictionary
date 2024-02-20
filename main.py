from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import os

import requests
from dotenv import load_dotenv

from utils import StatiFilesNoCache

load_dotenv()
MICROCMS_API_KEY=os.environ.get("MICROCMS_API_KEY")

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/words", response_class=HTMLResponse)
async def read_words(request: Request):
    res = requests.get('https://animal-dictionary.microcms.io/api/v1/words', headers={
        "X-MICROCMS-API-KEY": MICROCMS_API_KEY
    }, timeout=60)
    return res.text

@app.get("/words/{word}", response_class=HTMLResponse)
async def read_word(request: Request, word: str):
    return templates.TemplateResponse(
        request=request, name="word.html", context={"word": word}
    )

# サーチページのサンプル
@app.get("/search")
def read_root():
    return {"page": "Search Page"}

# 静的ファイルを設定
app.mount("/img-data", StatiFilesNoCache(directory="img-data",html=True), name="static")
app.mount("/", StatiFilesNoCache(directory="static",html=True), name="static")