from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import dou
from djini import parse_vacancies

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/dou")
def get_vacancies():
    return dou.parse_vacancies()

@app.get("/djini")
def get_djini_vacancies():
    return parse_vacancies()
