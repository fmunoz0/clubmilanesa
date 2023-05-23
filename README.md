# clubmilanesa

script to get an 20% off coupon in El Club de la Milanesa

store list
https://elclubdelamilanesa.com/cdm-panel/admin-ajax.php?action=store_search&lat=-34.53438&lng=-58.46789&search_radius=1000000

use "store" property in lowercase and replace blanks with underscores

example: "VICENTE LOPEZ" becomes "vicente_lopez"


# pseudocode

1) https://elclubdelamilanesa.com/online/vicente_lopez_delivery.php

2) extract url with "ide" param and do a GET request to it

3) extract properties "id_establishment", "auth" and "main_path" 

4) do a POST request to `https://"main_path"/ws/survey/scorecard/` with json content type and the form data:
```"{"email":"EMAIL_ADDRESS","id_establishment":"ID_ESTABLISHMENT"}"```

choose an email address and use the extracted "id_establishment"

add custom header:
"X-Server-Token: AUTH"

use "auth" string extracted before

5) save "id_scorecard" from response

6) do a PUT request to the previous url with same `X-Server-Token` header with following form data:

replace ID_SCORECARD, EMAIL_ADDRESS, ID_ESTABLISHMENT, NAME, AGE (in yyyy-mm-dd format)

```
{
  "id_scorecard": "ID_SCORECARD",
  "id_device": "",
  "lang": "es_AR",
  "email": "EMAIL_ADDRESS",
  "id_establishment": "ID_ESTABLISHMENT",
  "sender": "sys@thinkion.com.ar",
  "user": {
    "name": "NAME",
    "birth": "AGE"
  },
  "answers": [
    {
      "id": 10,
      "name": "CÓMO CALIFICAS TU EXPERIENCIA DE HOY?",
      "value": 100
    },
    {
      "id": 30,
      "name": "Cuando pedís por delivery, qué es más importante para vos?",
      "value": [
        "La comida"
      ]
    },
    {
      "id": 29,
      "name": "Porqué elegiste pedir en el Club de la Milanesa?",
      "value": [
        "Había una buena promo"
      ]
    },
    {
      "id": 0,
      "name": "Contanos lo que quieras",
      "value": ""
    }
  ],
  "device": {}
}
```
