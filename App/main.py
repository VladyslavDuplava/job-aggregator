from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import dou

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/vacancies")
def get_vacancies():
    return dou.parse_vacancies()
