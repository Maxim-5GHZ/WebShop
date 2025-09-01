from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse,PlainTextResponse
from pathlib import Path
import uvicorn
import socket

def get_local_ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        print(s.getsockname()[0])


app = FastAPI(title="HTML File Server")


HTML_DIR = Path("html")
PHOTO_DIR = Path("photo")

@app.get("/", response_class=HTMLResponse)
async def start_form():
        index_path = HTML_DIR / "startWindow.html"
        return FileResponse(index_path)


@app.get("/favicon.ico")
async def favicon():
    return PlainTextResponse(status_code=204)


if __name__ == "__main__":
    get_local_ip()

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )