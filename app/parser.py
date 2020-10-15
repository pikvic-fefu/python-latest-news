# Импортируем  необходимые пакеты: для запросов к сайтам и для разбора структуры веб-страниц
import requests
from bs4 import BeautifulSoup

# Словарь, содержащий ссылки на сайт и селектор для получения новостей
url_selector_dict = {
    'https://www.newsvl.ru/' : '.story-list__item-title > a',
    'https://www.rbc.ru/' : 'span[data-vr-headline]',
    'https://vestiprim.ru/' : '.short-news__item__title > a'
}

# Функция получения новостей с указанного сайта
def get_latest_news(url, selector):

    results = []

    # В переменную записываем ответ от запроса к сайту по адресу url
    response = requests.get(url)
    # Создаём экземпляр класса, который будет разбирать содержимое веб-страницы
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Выбираем необходимые html теги, содержащие заголовки новостей, согласно селектору
    items = soup.select(selector)
    print(f'Список новостей с сайта {url}:')

    # Цикл по всем найденным html тегам с заголовкам новостей, в котором печать текста каждого заголовка
    for item in items:
        results.append[item.text]

    return results

def parse_news():
    news = {}
    # Цикл по всем элементам словаря и вызов функции для каждого
    for url, selector in url_selector_dict.items():
        results = get_latest_news(url, selector)
        news[url] = results

    return news

