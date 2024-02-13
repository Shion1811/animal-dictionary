from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from utils import StatiFilesNoCache


app = FastAPI()

templates = Jinja2Templates(directory="templates")

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