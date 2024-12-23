# -*- coding: utf-8 -*-
from .bashim import Bashim


bash_quote = Bashim()
bash_quote.user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091112 Firefox/3.5.5'


def test_error():
    assert bash_quote.get_quote('qwe') == 'error'


def test_404():
    assert bash_quote.get_quote('3242342342342') == '404'


def test_get_quote():
    assert bash_quote.get_quote('12') == {
        'id': '12',
        'date': '30.08.2004 в 15:31',
        'raiting': '12415',
        'text': '\\* Takuto скоро будет мертв. Почему? А как вы думаете, можно спать под непрекращающийся кашель?\n<Hellcat> можно.\n<Hellcat> ты просто пристукни того, кто кашляет и мешает тебе спать.\n<Takuto> Хы. Тот кто кашляет - я. А пристукнут меня соседи.',
        'img': None
    }


def test_get_quote_img():
    assert bash_quote.get_quote('397136')[
        'img'] == 'https://xn--80abh7bk0c.xn--p1ai/img/r3wmd5802adqz6iu397136.jpg'
