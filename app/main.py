import random
import string

from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi import Request
from app.database import engine, SessionLocal
from app.models import Base, URL
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class URLRequest(BaseModel):
    url: str


def generate_short_code(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


@app.get("/")
def home():
    return {
        "message": "Welcome to Mouni's URL Shortener API"
    }


@app.get("/about")
def about():
    return {
        "description": "A simple URL shortener API",
        "project": "URL Shortener API",
        "developer": "Mouni"
    }


@app.get("/student")
def student():
    return {
        "name": "Mouni",
        "university": "Montclair State University",
        "course": "MS Computer Science"
    }


@app.get("/urls")
def get_urls(db: Session = Depends(get_db)):
    urls = db.query(URL).all()
    return urls


@app.post("/shorten")
def shorten_url(
    request: URLRequest,
    db: Session = Depends(get_db)
):
    short_code = generate_short_code()
    while db.query(URL).filter(URL.short_code == short_code).first():
        short_code = generate_short_code()

    new_url = URL(
        short_code=short_code,
        original_url=request.url,
        clicks=0
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {
        "original_url": request.url,
        "short_url": f"http://127.0.0.1:8000/{short_code}"
    }

@app.get("/analytics/top")
def get_top_urls(db: Session = Depends(get_db)):
    top_urls = (
        db.query(URL)
        .order_by(URL.clicks.desc())
        .limit(5)
        .all()
    )

    return top_urls


@app.delete("/url/{short_code}")
def delete_url(
    short_code: str,
    db: Session = Depends(get_db)
):
    url_record = (
        db.query(URL)
        .filter(URL.short_code == short_code)
        .first()
    )

    if not url_record:
        return {
            "error": "Short code not found"
        }

    db.delete(url_record)
    db.commit()

    return {
        "message": f"{short_code} deleted successfully"
    }


@app.get("/app")
def frontend(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.get("/url/{short_code}")
def get_url_by_code(
    short_code: str,
    db: Session = Depends(get_db)
):
    url_record = (
        db.query(URL)
        .filter(URL.short_code == short_code)
        .first()
    )

    if not url_record:
        return {
            "error": "Short code not found"
        }

    return url_record


