from fastapi import Response
from fastapi.staticfiles import StaticFiles


class StatiFilesNoCache(StaticFiles):
    def file_response(self, *args, **kwargs) -> Response:
        response = super().file_response(*args, **kwargs)
        response.headers["Cache-Contorol"] = "no-cache"
        return response
