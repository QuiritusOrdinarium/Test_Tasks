from bs4 import BeautifulSoup
import requests
import csv

animal_dict ={'А':0,'Б':0,'В':0,'Г':0,'Д':0,'Е':0,'Ё':0,'Ж':0,'З':0,'И':0,'Й':0,'К':0,
              'Л':0,'М':0,'Н':0,'О':0,'П':0,'Р':0,'С':0,'Т':0,'У':0,'Ф':0,
              'Х':0,'Ц':0,'Ч':0,'Ш':0,'Щ':0,'Э':0,'Ю':0,'Я':0
              }
url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
box = soup.find('div', class_='mw-category mw-category-columns')
#for litera in animal_dict.keys():
i = 0
litera=''
ContinueSearch=True
while ContinueSearch:
    for animal in box.find_all('a'):
        if litera=='':
            litera=animal.text[0]
            print(litera)
        else:
            if animal.text[0]==litera:
                i=i+1
                # print(i)
                # print(animal.text[0])
            else:
                print(animal.text)
                print(i)
                print(animal.text[0])
                print(litera)
                if litera in animal_dict.keys():
                    animal_dict[litera]=animal_dict[litera]+i
                else:
                    animal_dict[litera] = i
                print(animal_dict)
                #if animal.text[0]!='A':
                litera = animal.text[0]
                print(litera)
                i=1
                #else:
                #    ContinueSearch = False
                #    break
    if ContinueSearch==False:
        break
    else:
        link=soup.find(title='Категория:Животные по алфавиту',string='Следующая страница')
        if link!=None and box.find('h3',string='A')==None:
       # print(link)
            url = 'https://ru.wikipedia.org/'+link['href']
       # print(url)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            box = soup.find('div', class_='mw-category mw-category-columns')
        else:
            ContinueSearch = False
            break
print(animal_dict)
with open('beasts.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in animal_dict.items():
        writer.writerow(row)