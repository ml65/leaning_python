

import requests
from requests.auth import HTTPBasicAuth


def print_headers(response):
    if (response.status_code == 200):
        # обрабатываем полученные данные
        for key in response.headers:
            print(key, "=", response.headers[key])
    else:
        print('ERROR!', response.status_code, )


# GET
#print("====== GET =======\n")
response = requests.get('https://google.com')
#print_headers(response)
print(response.content)

'''
# POST
print("====== POST =======\n")
url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

response = requests.post(url, json = myobj)
print_headers(response)

# PUT
print("====== PUT =======\n")

response = requests.put('http://example.com/api/resource',
                        json={'key': 'value'},
                        auth=HTTPBasicAuth('username', 'password'))
print_headers(response)
print(response.status_code)  # Если ответ не 200, значит возникли проблемы


# DELETE
print("====== DELETE =======\n")
response = requests.delete('https://books.ru/1231231')
print_headers(response)
'''