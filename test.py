import sys
from io import BytesIO
import requests
from PIL import Image
import geocoder

# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:
toponym_to_find = " ".join(sys.argv[1:])
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json",
}
response = requests.get(geocoder_api_server, params=geocoder_params)
json_response = response.json()

# Получаем первый топоним из ответа геокодера.
toponym = (
    json_response.get("response")
    .get("GeoObjectCollection")
    .get("featureMember")[0]
    .get("GeoObject")
)

# Собираем параметры для запроса к StaticMapsAPI:
ll = geocoder.get_ll(toponym)
spn = geocoder.get_spn(toponym)
map_params = {
    "l": "map",
    "ll": ll,
    "spn": spn,
    "pt": ll + ",pm2blywl",
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(response.content)).show()
# Создадим картинку
# и тут же ее покажем встроенным просмотрщиком операционной системы
