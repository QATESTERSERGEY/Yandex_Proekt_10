import configuration
import requests
import data

# Создатние набора с заданым имене
def get_kit_body(name):
    current_name = data.kit_body.copy()
    current_name["name"] = name
    return current_name
# Создать нового пользователя и возрашение токкена
def get_new_user_token():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, headers=data.headers, json=data.user_body)
    return response.json()['authToken']
# Создатние набора с токеном пользователя с заданным именем набора
def get_kits(authToken, kit_data):
    headers = data.headers.copy()
    headers["Authorization"] = "Bearer " + authToken
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_MAIN_KITS_PATH, headers=headers, json=kit_data)