import requests
import re
import json

# configure this first!
# store list: https://elclubdelamilanesa.com/cdm-panel/admin-ajax.php?action=store_search&lat=-34.53438&lng=-58.46789&search_radius=1000000
# use "store" property in lowercase and replace blanks with underscores
STORE = "vicente_lopez"
EMAIL = "foobar@example.com"
NAME = "John Doe"
BIRTH = "1991-01-01"

r = requests.get("https://elclubdelamilanesa.com/online/{}_delivery.php".format(STORE))
url = re.search(r'https://[^/]*/\?ide=[^"]*', r.text).group(0)
#print(url)

r = requests.get(url)
id_establishment = re.search(r'"id_establishment":"([^"]*)"', r.text).group(1)
main_path = re.search(r'"main_path":"([^"]*)"', r.text).group(1).replace('\\', '')
auth = re.search(r'"auth":"([^"]*)"', r.text).group(1)
#print(id_establishment, main_path, auth)

headers = { 'Content-Type': 'application-json', 'X-Server-Token': auth }
data = { 'email': EMAIL, 'id_establishment': id_establishment }
r = requests.post(main_path + 'ws/survey/scorecard/', headers=headers, data=json.dumps(data))
id_scorecard = r.json().get('id_scorecard')
#print(id_scorecard)

data = {
  'id_scorecard': id_scorecard,
  'id_device': '',
  'lang': 'es_AR',
  'email': EMAIL,
  'id_establishment': id_establishment,
  'sender': 'sys@thinkion.com.ar',
  'user': {
    'name': NAME,
    'birth': BIRTH
  },
  'answers': [
    {
      'id': 10,
      'name': 'CÓMO CALIFICAS TU EXPERIENCIA DE HOY?',
      'value': 100
    },
    {
      'id': 30,
      'name': 'Cuando pedís por delivery, qué es más importante para vos?',
      'value': [
        'La comida'
      ]
    },
    {
      'id': 29,
      'name': 'Porqué elegiste pedir en el Club de la Milanesa?',
      'value': [
        'Había una buena promo'
      ]
    },
    {
      'id': 0,
      'name': 'Contanos lo que quieras',
      'value': ''
    }
  ],
  'device': {}
}

r = requests.put(main_path + 'ws/survey/scorecard/', headers=headers, data=json.dumps(data))
print(r.json().get('code'))






