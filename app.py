from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/create", response_class=HTMLResponse)
async def create_comic(
    request: Request,
    character: str = Form(...),
    story: str = Form(...)
):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "character": character,
            "story": story,
            "result": f"Comic idea created for {character}: {story}"
        }
    )
