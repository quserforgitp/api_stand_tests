import sender_stand_request
import data

def get_user_body(name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    user_body_copy = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    user_body_copy["firstName"] = name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return user_body_copy

# Función de prueba positiva
def positive_assert(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)
    # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable user_response
    user_response = sender_stand_request.post_new_user(user_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201, "El codigo de estado de la respuesta HTTP deberia de ser 201 indicando que el recurso fue creado con exito"
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != "", "El campo authToken deberia estar presente y ademas deberia tener un valor"

    # El resultado de la solicitud de recepción de datos de la tabla "user_model" se guarda en la variable "users_table_response"
    users_table_response = sender_stand_request.get_users_table()

    # String que debe estar en el cuerpo de respuesta
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    # Comprueba si el usuario o usuaria existe y es único/a
    assert users_table_response.text.count(str_user) == 1

# Funcion de prueba negativa
def negative_assert_symbol(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)
    # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable user_response
    user_response = sender_stand_request.post_new_user(user_body)

    # Comprueba si el código de estado es 400 bad request
    assert user_response.status_code == 400, "El codigo de estado de la respuesta HTTP deberia de ser 400 indicando un bad request por parte de quien envia la peticion"
    # Comprueba que el campo code está en la respuesta y contiene el valor 400
    assert user_response.json()["code"] == 400, "El codigo de respuesta de estado HTTP en el campo code de la respuesta deberia de ser 400 indicando un bad request por parte de quien envia la peticion"

    # String que debe estar en el cuerpo de respuesta
    str_message = "Has introducido un nombre de usuario no válido. El nombre solo puede "\
 "contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."

    # Comprueba si el valor del campo message es correcto
    assert str_message == user_response.json()["message"], "El texto del message deberia de coincidir con el esperado"

# Prueba 1. Creación de un nuevo usuario o usuaria
# El parámetro "firstName" contiene dos caracteres
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

# Prueba 2. Creación de un nuevo usuario o usuaria
# El parámetro "firstName" contiene 15 caracteres
def test_create_user_15_letters_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

# Prueba 3. Error
# El parámetro "firstName" contiene un carácter
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")

# Prueba 4. Error
# El parámetro "firstName" contiene 16 carácteres
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Аааааааааааааааа")

# Prueba 5. Error
# El parámetro "firstName" contiene palabras con espacios
def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A Aaa")

# Prueba 6. Error
# El parámetro "firstName" contiene un string de caracteres especiales
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",")

# Test 7. Error
# El parámetro "firstName" contiene un string de números
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")

# Función de prueba negativa
# La respuesta contiene el siguiente mensaje de error: "No se han enviado todos los parámetros requeridos"
def negative_assert_no_firstname(user_body):
    # Guarda el resultado de llamar a la función a la variable "response"
    response = sender_stand_request.post_new_user(user_body)

    # Comprueba si la respuesta contiene el código 400
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

# Prueba 8. Error
# La solicitud no contiene el parámetro "firstName"
def test_create_user_no_first_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    # De lo contrario, se podrían perder los datos del diccionario de origen
    user_body = data.user_body.copy()
    # El parámetro "firstName" se elimina de la solicitud
    user_body.pop("firstName")
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)

# Prueba 10. Error
# El tipo del parámetro "firstName" es un número
def test_create_user_number_type_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(12)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    response = sender_stand_request.post_new_user(user_body)

    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400