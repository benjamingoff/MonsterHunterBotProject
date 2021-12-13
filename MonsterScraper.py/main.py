# BWG, 121221, Program to grab as many monster stats from the wiki as I can

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

# Const of all of the habitats in MHRise in order to parse them out of the list of all monster hunter games
MONSTER_HABITATS = ['Frost Islands', 'Sandy Plains', 'Flooded Forest (Rise)', 'Lava Caverns',
                    'Red Stronghold', 'Coral Palace', 'Infernal Springs', 'Shrine Ruins']

# Base URL to the Wiki I hit off of
BASE_URL = 'https://monsterhunter.fandom.com/wiki/'

monsterDictionary = dict()
monsterList = []

# Open the master list of monster, read it in, split it into a list of said monsters
with open(r'venv\MonsterList.txt', 'r') as f:
    listAsString = f.read().replace('\n', '')
    monsterList = listAsString.split(',')


# Gets the name from the title of the page's html
def getName():
    title = soup.find('h1', attrs={'class': 'page-header__title'})
    monsterName = title.text.strip()

    if monsterName:
        return monsterName

    return None


# Returns a list of habitats that match the ones in the master list of Rise habitats.  Filters out old MH Maps
def getHabitats():
    habitatTable = soup.find_all('div', attrs={'class': 'pi-item pi-data pi-item-spacing pi-border-color'
        , 'data-source': 'Habitats'})

    habitatsList = []

    for i in MONSTER_HABITATS:
        htmlToString = str(habitatTable).lower()
        if htmlToString.find(i.lower()) != -1:
            habitatsList.append(i)

    return habitatsList


# Gets the table for the monsters hitzones/elemental/ailment weaknesses.  ONLY works on rise monster pretty much.
def getHitzoneDamageData():
    damageTable = soup.find_all('table', attrs={'class': 'wikitable', 'width': '100%'})
    masterList = []
    for table in damageTable:
        tableList = []
        body = table.find('tbody')
        rows = body.find_all('tr')
        for i in rows:
            rowList = []
            data = i.find_all('td')
            for j in data:
                rowList.append(j.text.strip())

            removeEmptyRows = [ele for ele in rowList if ele != []]
            if len(removeEmptyRows):
                tableList.append(removeEmptyRows)

        masterList.append(tableList)

    return masterList


# Maps said hitzones to a dictionary to be turned into JSON later
def monsterHitzonesToDict(hitzones):
    hitzoneDictionary = dict()
    for area in hitzones:
        try:
            hitzoneDictionary[area[0]] = {'Cutting': area[1], 'Impact': area[2], 'Shot': area[3]}
        except:
            print('Error writing to hitzone dictionary')

    return hitzoneDictionary


# Maps said elemental weaknesses to a dictionary to be turned into JSON later
def monsterElementWeaknessToDict(weaknesses):
    elementalDictionary = dict()
    for area in weaknesses:
        try:
            elementalDictionary[area[0]] = {'Fire': area[1], 'Water': area[2], 'Thunder': area[3], 'Ice': area[4],
                                            'Dragon': area[5]}
        except:
            print('Error writing to elemental dictionary')

    return elementalDictionary


# Maps said ailments weaknesses to a dictionary to be turned into JSON later
def monsterAilmentsToDictionary(ailments):
    ailmentsDictionary = dict()
    for ailment in ailments:
        try:
            ailmentsDictionary[ailment[0]] = len(ailment[1])
        except:
            print('Error writing to ailment dictionary')

    return ailmentsDictionary


# Going through and scraping all of the monsters in the game
for i in monsterList:
    # Gets the html from the wiki, parses it using bs4
    url = BASE_URL + i
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    monsterName = getName()
    monsterHabitats = getHabitats()
    damageTables = getHitzoneDamageData()

    # Here I'm just trying to split up the tables since it grabs all 3.  If it can't find them, it will just default
    # to empty lists and bail out
    try:
        monsterHitzones = damageTables[0]
        monsterElemental = damageTables[1][1:]
        monsterAilments = []
        for j in damageTables[2]:
            monsterAilments.append(tuple(j[:2]))
            monsterAilments.append(tuple(j[2:]))
    except:
        monsterHitzones = []
        monsterElemental = []
        monsterAilments = []

    # Try and map all of these lists I've made to dictionaries for easy JSON
    try:
        monsterDictionary[monsterName] = {"habitats": monsterHabitats,
                                          "hitzones": monsterHitzonesToDict(monsterHitzones),
                                          "elements": monsterElementWeaknessToDict(monsterElemental),
                                          "ailments": monsterAilmentsToDictionary(monsterAilments)}
    except:
        print('ERROR WRITING ' + i + ' TO DICTIONARY')

# Write the dictionary to JSON.
with open('monsters.json', 'w') as outfile:
    json.dump(monsterDictionary, outfile)
