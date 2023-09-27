import sender_stand_request

# Функция для позитивной проверки по вводимым символам
# Проверка успешного создания набора с измененным именем под
# авторизованным пользователем code = 201
def positive_assert(name):
    authToken = sender_stand_request.get_new_user_token()
    kit = sender_stand_request.get_kit_body(name)
    kits_response = sender_stand_request.get_kits(authToken, kit)
    assert kits_response.status_code == 201
    assert kits_response.json()["name"] == kit["name"]
# Функция для негативной проверки по вводимым символам
# Ошибка. Набор не создан под авторизованным пользователем
# code = 400 при введеных/не введенных символах
def negative_assert_code_400(name):
    authToken = sender_stand_request.get_new_user_token()
    body = sender_stand_request.get_kit_body(name)
    kits_response = sender_stand_request.get_kits(authToken, body)
    assert kits_response.status_code == 400

# Тест 1. Допустимое количество символов (1)
# Параметр name состоит из 1 символа (а)
def test_create_kit_1_letter_in_kit_body_get_success_response():
    positive_assert("a")

# Тест 2. Допустимое количество символов (511)
# Параметр name состоит из 511 символов
def test_create_kit_511_letter_in_kit_body_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC");

# Тест 3. Ошибка. Количество символов меньше допустимого (0)
# Параметр name состоит из 0 символов (пустая строка)
def test_create_kit_0_letter_in_kit_body_get_failed_response():
    negative_assert_code_400("")

# Тест 4. Ошибка. Количество символов больше допустимого (512)
# Параметр name состоит из 512 символов (512 символов латиницы/кирилицы)
def test_create_kit_512_letter_in_kit_body_get_failed_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD");

# Тест 5. Разрешены английские буквы
# Параметр name состоит из английский букв (QWErty)
def test_create_kit_english_letter_in_kit_body_get_success_response():
    positive_assert("QWErty")

# Тест 6. Разрешены русские буквы
# Параметр name состоит из русских букв (Мария)
def test_create_kit_russian_letter_in_kit_body_get_success_response():
    positive_assert("Мария")

# Тест 7. Разрешены спецсимволы
# Параметр name состоит из спецсимволов ("№%@,)
def test_create_kit_special_characters_in_kit_body_get_success_response():
    positive_assert("\"№%@\,")

# Тест 8. Разрешены пробелы
# Параметр name состоит из пробелов (Человек и Ко)
def test_create_kit_space_in_kit_body_get_success_response():
    positive_assert("Человек и КО")

# Тест 9. Разрешены цифры
# Параметр name состоит из цифр (123)
def test_create_kit_number_in_kit_body_get_success_response():
    positive_assert("123")

# Тест 10. Ошибка. Параметр не передан в запросе
# В запросе параметр name - не передан
def test_create_kit_no_params_in_kit_body_get_failed_response():
    authToken = sender_stand_request.get_new_user_token()
    kits_response = sender_stand_request.get_kits(authToken, {})
    print(kits_response.json())
    assert kits_response.status_code == 400

# Тест 11. Ошибка. Передан другой тип параметра
# В запросе параметр name - передан числом
def test_create_kit_other_type_of_params_in_kit_body_get_failed_response():
    negative_assert_code_400(123)