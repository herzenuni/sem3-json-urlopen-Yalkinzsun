На основе кода с выполнением предыдущего задания (https://github.com/herzenuni/sem3-assignment3-081217-Yalkinzsun) реализуйте получение JSON с удаленного хоста и красивый вывод информации на экран. 

В качестве хоста может быть использован один из сервисов/страниц, предложенных ниже: 

    △ json-файл с данными из предыдущего задания
    △ users.get (см. страницу с описанием ниже)
    △ API GitHub Jobs (страница описание API: https://jobs.github.com/api)
    △ репозиторий со списком API (смотрите те, у которых в таблице поле "Auth" стоит значение "None")
    △ API vk.com по ссылке: https://vk.com/dev/first_guide, https://vk.com/dev/users.get

Фрагмент кода для получения данных по URL-адресу:
```python
request = "https://api.vk.com/method/users.get?user_ids = 1,md&v=5.8&fields=status, online"

from urllib.request import urlopen
request_data = urlopen(request)
