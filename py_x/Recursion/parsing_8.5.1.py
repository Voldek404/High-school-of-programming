import json
import requests
from bs4 import BeautifulSoup
post_process = requests.post('http://httpbin.org/post', data = {'UserId':'12345', 'Status':'On'})
if post_process.status_code == 200:
    print("Запрос отправлен успешно")
    print("Ответ от сервера:", post_process.text)
else:
    print(f"Ошибка: {post_process.status_code}")
