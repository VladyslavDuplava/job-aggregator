from typing import Dict
from bs4 import BeautifulSoup
import requests

url = "https://djinni.co/jobs/?search_type=basic-search&primary_keyword=Python&page=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def parse_vacancies() -> list[dict]:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    vacancies = []

    for job in soup.find_all("div", class_="job-item card-link fs-5 mb-4 rounded-2 p-2"):
        title = job.find("div", class_="fw-medium d-flex flex-wrap align-items-center column-gap-1")
        link = job.find("a", class_="job_item__header-link d-flex flex-column gap-1 text-decoration-none")
        description = job.find("div", class_="col")
        vacancies.append({
            "title": title.get_text(strip=True),
            "link": link.get("href"),
            "description": description.get_text(strip=True),
        })

    return vacancies
