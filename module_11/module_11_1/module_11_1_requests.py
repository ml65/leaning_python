# Домашнее задание по теме "Обзор сторонних библиотек Python"

# requests - запросить данные с сайта и вывести их в консоль.

import requests
import re
# GET
url = 'https://lipsum.com/'
response = requests.get(url)

# вывод текста
res = re.sub(r"<[^>]+>", "", response.text, flags=re.S)
print(res)

# вывод html
#print(response.content)


