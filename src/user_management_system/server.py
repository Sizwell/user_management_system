from pathlib import Path
from typing import Union

from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
app.mount("/static",
          StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
          name="static",
          )

templates = Jinja2Templates(directory="templates")

@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html",
                                      context={'request': request}
                                      )
