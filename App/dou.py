from bs4 import BeautifulSoup
import requests

url = "https://jobs.dou.ua/vacancies/?category=Python&exp=1-3"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

def parse_vacancies() -> list[dict]:
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml') #bs object
        vacancies = []
        for a in soup.find_all('a', class_='vt'):
            vacancies.append({
                "title": a.get_text(strip=True),
                "link": a.get('href',)
            })
        return vacancies
    return None