import requests
from bs4 import BeautifulSoup
from selenium import webdriver

text = ''

def modText(string):
    global text

    text += string + '\n'

'''driver = webdriver.Firefox()

# Navigate to website
driver.get('https://statsroyale.com/clan/LRPCRP92/war/')

# Find the button element and click it
button = driver.find_element_by_id('button_id')
button.click()'''

url = 'https://statsroyale.com/clan/LRPCRP92/war'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup)

#modText(soup)

info = soup.find_all('div', class_='clanParticipants__row')

nums = []
names = []
attacks = []
medals = []

for i in range(0,len(info),6):
    num = info[i].text.strip()
    name = info[i+1].text.strip()
    attack = info[i+2].text.strip()
    #dontcare = info[i+3].text
    #dontcare = info[i+4].text
    medal = info[i+5].text.strip()

    nums.append(num)
    names.append(name)
    attacks.append(attack)
    medals.append(medal)

    #modText(f"{num} {name} | Attacks: {attack} Medals: {medal}")


url = 'https://statsroyale.com/clan/LRPCRP92'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

members = soup.find_all('a', 'ui__blueLink')

inClan = []

for i in range(len(names)):
    for n in range(len(members)):
        if members[n].text.strip() == names[i]:
            inClan.append(i)


for i in range(len(attacks)):
    attacks[i] = int(attacks[i])
    medals[i] = int(medals[i])

avgMed = 0
avgAtt = 0

for i in range(len(inClan)):
    avgAtt += attacks[inClan[i]]
    avgMed += medals[inClan[i]]

    nam = str(names[inClan[i]]).ljust(16,' ')
    att = str(attacks[inClan[i]]).rjust(2,' ')
    med =  str(medals[inClan[i]]).rjust(4, ' ')

    modText(nam + f"| Attacks: {att} Medals: {med}")

avgAtt = avgAtt/len(inClan)

avgMed = avgMed/len(inClan)

modText("__________________________________________\n")

modText(f"Average Attacks: {round(avgAtt, 2)} | Average Medals: {round(avgMed, 2)}")

print(text)


##LRPCRP92