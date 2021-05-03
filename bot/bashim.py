# -*- coding: utf-8 -*-
import os
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

class Bashim:

    def __init__(self):
        self.bashim_url = 'https://bash.im'
        self.user_agent = os.environ.get("USER_AGENT")
        self.markdown_sanitize = ['*', '_', '`', '[']

    def _get_html(self, url):
        request = Request(self.bashim_url + url)
        request.add_header('User-agent', self.user_agent)
        try:
            req = urlopen(request)
            # Если страницы нет, то происходит редирект на главную, проверяем.
            if req.geturl() == self.bashim_url + '/':
                return '404'
            else:
                req = req.read().decode('utf-8', 'ignore')
                return self._get_quote_data(req)
        except Exception:
            return 'error'

    def _get_quote_data(self, html):
        quotes = BeautifulSoup(html, 'html.parser')
        quote = quotes.find('article', attrs={'class': 'quote'})

        # Получаем текст цитаты
        quote_text = quote.find('div', attrs={'class': 'quote__body'})
        if quote_text is not None:
            quote_text = quote_text.get_text('\n', strip=True)
            # Экранируем символы markdown
            for char in self.markdown_sanitize:
                quote_text = quote_text.replace(char, '\\' + char)

        # Получаем id цитаты.
        quote_id = quote.find('a', attrs={'class': 'quote__header_permalink'})
        if quote_id is not None:
            quote_id = quote_id.get('href').replace('/quote/','')

        # Получаем дату публикации.
        quote_date = quote.find('div', attrs={'class': 'quote__header_date'})
        if quote_date is not None:
            quote_date = quote_date.get_text(strip=True)

        # Получаем рейтинг цитаты.
        quote_raiting = quote.find('div', attrs={'class': 'quote__total'})
        if quote_raiting is not None:
            quote_raiting = quote_raiting.get_text(strip=True)

        # Получаем комикс, если он есть.
        quote_img = None
        quote_img_el = quote.find('img', attrs={'class': 'quote__strips_img'})
        if quote_img_el is not None:
            quote_text = quote_text.replace('\nКомикс по мотивам цитаты','')
            quote_img = self.bashim_url + quote_img_el['src'].replace('ts/','')
                
        # Возвращаем цитату со всей инфой.
        return {'id': quote_id,
                'date': quote_date,
                'raiting': quote_raiting,
                'text': quote_text,
                'img': quote_img}

    def get_random_quote(self):
        return self._get_html('/random')

    def get_quote(self, id):
        return self._get_html( '/quote/' + str(id))

if __name__ == '__main__':
    quote =  Bashim()
    quote.user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091112 Firefox/3.5.5'
    print(quote.get_quote(397136))
    #print(quote.get_quote(12))
    #print(quote.get_random_quote())