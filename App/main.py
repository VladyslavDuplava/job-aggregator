from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import dou
from djini import parse_vacancies
from Schemas import Vacancy

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/dou", response_model = list[Vacancy])
def get_vacancies():
    return dou.parse_vacancies()

@app.get("/djini", response_model = list[Vacancy])
def get_djini_vacancies():
    return parse_vacancies()
