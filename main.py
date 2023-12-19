import requests

from bs4 import BeautifulSoup


# headers = {

#     'accept': '*/*',

#     # 'user-agent': 'Mozilla/5.0 (Linux; Android 7.1; Xperia V Build/NDE63X) AppleWebKit/600.3 (KHTML, like Gecko)  Chrome/55.0.2635.298 Mobile Safari/533.5',

# }

for i in range(1,4):

    print(f'Парсим {i}-ю стр...')

   

    url = f'https://www.olx.kz/list/q-%D0%B5%D0%BB%D0%BA%D0%B8/?page={i}'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')
    cards=soup.find_all('div',attrs={'data-testid':'l-card'})
    count=0
    for card in cards[:5]:
        
        card_url = card.a['href']

        url = f'https://www.olx.kz{card_url}'

        response = requests.get(url=url)

        soup = BeautifulSoup(response.text, 'lxml')

        description = soup.find("div", class_='css-1t507yq er34gjf0')
        count+=1
        print(f"Объявление №{count} \n")
        print(f'{description.text} \n')