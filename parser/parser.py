import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = 'https://libcat.ru'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='tg-postbook')
    manas_flm = []

    for item in items:
        manas_flm.append(
            {
                'title': item.find('div', class_='h3').find('a').get('href'),
                'title_text': item.find('span', class_='tg-bookwriter mb-5 font-bold').get_text(),
                'image': URL + item.find('div', class_='tg-backcover').find('img').get('src')
            }
        )
    return manas_flm

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        quiz = []
        for page in range(0, 1):
            html = get_html(f'https://libcat.ru/knigi/nauka-i-obrazovanie', params=page)
            quiz.extend(get_data(html.text))
        return quiz
    else:
        raise Exception('Error in parser func........')
