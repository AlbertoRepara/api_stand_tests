import sender_stand_request
import data
# esta función cambia los valores en el parámetro "firstName"
def get_user_body(first_name):
    current_body = data.user_body.copy()  #el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body["firstName"] = first_name # Se cambia el valor del parámetro firstName
    return current_body    # Se devuelve un nuevo diccionario con el valor firstName requerido

"""
print(data.user_body)# imprimir los datos que tienes en user_body
print(get_user_body("A"))# imprimir el valor que le das a 
"""
def positive_assert(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1
#pruebas negativas
def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
    assert user_response.json()["message"] == 'Has introducido un nombre de usuario no válido. El nombre solo puede '\
                                                'contener letras del alfabeto latino, la longitud debe ser de 2 a 15 '\
                                                 'caracteres.'
def negative_assert_no_first_name(user_body):
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == 'No se han aprobado todos los parámetros requeridos'


def test_create_user_2_letter_in_first_name_get_success_response():#funcion para probar probar con 2 letras
    positive_assert("Aa")
def test_create_user_15_letter_in_first_name_get_success_response():#funcion para probar probar con 15 letras
    positive_assert("Aaaaaaaaaaaaaaa")

def test_create_user_1_letter_in_first_name_get_success_response():#funcion para probar probar con 1 letra
    negative_assert_symbol("a")
def test_create_user_16_letter_in_first_name_get_success_response():#funcion para probar probar con 16 letras
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")

def test_create_user_has_space_in_first_name_get_error_response():#funcion para probar probar con espacios en el string
    negative_assert_symbol("Alberto Santillan")# la prueba debe pasar por que validamos un 400

def test_create_user_has_special_symbol_in_first_name_get_error_response():#validacion caracteres especiales
    negative_assert_symbol("\"№%@\",")# la prueba debe pasar por que validamos un 400

def test_create_user_has_number_in_first_name_get_error_response(): #validacion de numeros enteros
    negative_assert_symbol("123") #debe pasar la prueba por que buscamos un 400

def test_create_user_no_first_name_get_error_response():# prueba 8
    user_body = data.user_body.copy()
    user_body.pop("firstName")
    negative_assert_no_first_name(user_body)

def test_create_user_empty_first_name_get_error_response():# prueba 9
    user_body = get_user_body(" ")
    user_body.pop("firstName")
    negative_assert_no_first_name(user_body)

def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400

