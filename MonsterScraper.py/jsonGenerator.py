# BWG 121321: Program to create a json file for the missing monsters so I don't have to do everything by hand

import json

partsList = ['Head','Neck','Foreleg','Abdomen','Back','Wing','Hind Leg', 'Tail']
ailmentsList = ['Poison', 'Stun', 'Paralysis', 'Sleep', 'Blast', 'Exhaust', 'Fireblight', 'Waterblight',
                'Thunderblight', 'Iceblight']

hitzones = [60,55,35,40,35,25,45,50,35,35,50,34,23,25,30,23,23,20,30,30,25,35,30,35]

elements = [10,5,15,0,10,10,5,15,0,5,10,5,20,0,10,10,5,15,0,10,10,5,15,0,10,10,5,20,0,15,10,5,15,0,5,10,5,20,0,15]

ailments = [1,1,0,0,3,0,1,1,2,1]

hitzoneDictionary = dict()
elementDictionary = dict()
ailmentDictionary = dict()
try:
    for zone in range(0,len(hitzones), 3):
        hitzoneDictionary[partsList[zone // 3]] = {'Cutting': str(hitzones[zone]), 'Impact': str(hitzones[zone+1]),
                                              'Shot': str(hitzones[zone + 2])}
except:
    print('Error in Hitzone write')

for area in range(0, len(elements), 5):
    elementDictionary[partsList[area // 5]] = {'Fire': str(elements[area]), 'Water': str(elements[area + 1]),
                                          'Thunder': str(elements[area + 2]), 'Ice': str(elements[area + 3]),
                                          'Dragon': str(elements[area + 4])}

for ailment in range(len(ailmentsList)):
    ailmentDictionary[ailmentsList[ailment]] = ailments[ailment]

masterDictionary = {"hitzones": hitzoneDictionary,
                    "elements": elementDictionary,
                    "ailments": ailmentDictionary}

with open('temp.json', 'w') as outfile:
    json.dump(masterDictionary, outfile)
