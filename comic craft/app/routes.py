from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .gemini_flash import generate_story
from .gemini_pro import generate_detailed_story


# Create router
router = APIRouter()

# Tell FastAPI where the HTML templates are located
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Display the Comic Craft home page.
    """

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


@router.post("/generate", response_class=HTMLResponse)
async def generate_comic(
    request: Request,
    prompt: str = Form(...)
):
    """
    Generate a comic story from the user's prompt.
    """

    try:
        # Generate the basic comic story
        story = generate_story(prompt)

        return templates.TemplateResponse(
            "comic_preview.html",
            {
                "request": request,
                "prompt": prompt,
                "story": story,
                "panels": []
            }
        )

    except Exception as e:

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": str(e)
            }
        )


@router.post("/generate-detailed", response_class=HTMLResponse)
async def generate_detailed_comic(
    request: Request,
    prompt: str = Form(...)
):
    """
    Generate a more detailed comic story.
    """

    try:
        # Generate detailed story
        story = generate_detailed_story(prompt)

        return templates.TemplateResponse(
            "comic_preview.html",
            {
                "request": request,
                "prompt": prompt,
                "story": story,
                "panels": []
            }
        )

    except Exception as e:

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": str(e)
            }
        )