from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

url = "https://djinni.co/jobs/?search_type=basic-search&primary_keyword=Python&exp_level=1y&exp_level=2y&exp_level=3y"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def parse_vacancies() -> list[dict]:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    vacancies = []

    for job in soup.find_all("div", class_="job-item card-link fs-5 mb-4 rounded-2 p-2"):
        title = job.find("h2", class_="job-item__position fs-4 m-0 mb-1")
        params = job.find("div", class_="fw-medium d-flex flex-wrap align-items-center column-gap-1")
        link = job.find("a", class_="job_item__header-link d-flex flex-column gap-1 text-decoration-none")
        description = job.find("div", class_="col")

        vacancies.append({
            "title": title.get_text(" ", strip=True),
            "details": params.get_text(" ", strip=True),
            "link": urljoin("https://djinni.co", link.get("href")),
            "description": description.get_text(" ",strip=True) if description else None,
            "source": "djini"
        })

    return vacancies
