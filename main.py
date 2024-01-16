from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/search")
def read_root():
    return {"page": "Search Page"}
app.mount("/img-data", StaticFiles(directory="img-data",html=True), name="static")
app.mount("/", StaticFiles(directory="static",html=True), name="static")
