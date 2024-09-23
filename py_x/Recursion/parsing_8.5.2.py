from bs4 import BeautifulSoup
import requests
final_list = []
for i in range(1,6):
    response = requests.get(f'https://rosseti-lenenergo.ru/tenders/?PAGEN_1={i}&tab=1')
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html5lib")
        tender_list = soup.find_all('td', {'class': 'item-cell-3'})
    for item in tender_list:
        if "Модернизация" in item.text:
            final_list.append(item.text)
print(set(final_list))
