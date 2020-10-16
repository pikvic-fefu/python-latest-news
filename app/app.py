# Импортируем  необходимые пакеты: для запросов к сайтам и для разбора структуры веб-страниц
import datetime
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

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
    # Цикл по всем найденным html тегам с заголовкам новостей, в котором печать текста каждого заголовка
    for item in items:
        results.append(item.text)
    return results

def parse_news():
    news = []
    # Цикл по всем элементам словаря и вызов функции для каждого
    for url, selector in url_selector_dict.items():
        results = get_latest_news(url, selector)
        news.append({'url' : url, 'results': results})
    return news


app = Flask(__name__)

latest_news = parse_news()
last_date = datetime.datetime.now()

@app.route("/")
def get_latest_news():
    global latest_news
    if (datetime.datetime.now() - last_date).seconds > 1800:
        latest_news = parse_news()
    return render_template("index.html", latest_news=latest_news)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
