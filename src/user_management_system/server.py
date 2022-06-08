from pathlib import Path
from typing import Union

import database
import uvicorn
from fastapi import FastAPI, Form
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

@app.get("/forms", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("forms-wizard.html",
                                      context={'request': request}
                                      )

@app.post("/submit_doc", response_class=HTMLResponse)
async def doc_info(request: Request,
             username: str = Form(...),
             password: str = Form(...),
             firstname: str = Form(...),
             lastname: str = Form(...),
             ccnumber: str= Form(...),
             email: str = Form(...)
             ):
    print("User name: ", username,
          "\nFirst Name: ", firstname,
          "\nLast Name: ", lastname,
          "\nEmail: ", email,
          "\nCard Number: ", ccnumber,
          "\nPassword: ", password
          )


if __name__ == '__main__':
    uvicorn.run(app)