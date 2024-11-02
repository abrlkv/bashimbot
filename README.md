# Telegram bash.im bot
[Бот](https://t.me/randobash_bot) позволяет получать цитаты с сайта [башорг](https://башорг.рф)
Для получения рандомной цитаты, отправьте боту любое сообщение или нажмите на кнопку "Показать еще".
Для получения конкретной цитаты отправьте id цитаты.

Написан с использованием [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

## Запуск с помомощью docker-compose
```yml
basimbot:
  image: abrlkv/bashimbot
  restart: always
  environment:
    - API_TOKEN=Telegram API token
    - USER_AGENT=Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091112 Firefox/3.5.5
```
## Скриншоты
 ![screenshot](https://i.imgur.com/pJLRbDg.png)