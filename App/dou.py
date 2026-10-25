from bs4 import BeautifulSoup
import requests
    
url = "https://jobs.dou.ua/vacancies/?category=Python&exp=1-3"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}



def parse_vacancies() -> list[dict]:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml') #bs object
    vacancies = []

    for a in soup.find_all('li', class_='l-vacancy'):
        title = a.find('a', class_='vt')
        date = a.find('div', class_='date')
        locatation = a.find('span', class_='cities')


        vacancies.append({
            "title": title.get_text(strip=True),
            "date": date.get_text(strip=True) if date else None,
            "location": locatation.get_text(strip=True) if locatation else None,
            "link": title.get('href',),
            "source": "dou"

        })
    return vacancies
