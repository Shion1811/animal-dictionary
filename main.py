from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles

class StatiFilesNoCache(StaticFiles):
    def file_response(self, *args, **kwargs) -> Response:
        response = super().file_response(*args, **kwargs)
        response.headers["Cache-Contorol"] = "no-cache"
        return response

app = FastAPI()

@app.get("/search")
def read_root():
    return {"page": "Search Page"}
app.mount("/img-data", StaticFiles(directory="img-data",html=True), name="static")
app.mount("/", StatiFilesNoCache(directory="static",html=True), name="static")
