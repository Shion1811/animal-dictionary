from fastapi import FastAPI

from utils import StatiFilesNoCache


app = FastAPI()

# サーチページのサンプル
@app.get("/search")
def read_root():
    return {"page": "Search Page"}

# 静的ファイルを設定
app.mount("/", StatiFilesNoCache(directory="static",html=True), name="static")
app.mount("/img-data", StatiFilesNoCache(directory="img-data",html=True), name="static")