
---

# 🚀 **API User Creation Tests**  
Automated test suite to validate user creation via API. Ensures compliance with input validation rules for the `firstName` parameter.

---

## 📝 **Descripción**  
Este proyecto contiene pruebas automatizadas para validar el endpoint de creación de usuarios. Se comprueban casos positivos y negativos según las reglas del negocio.

---

## 📋 **Requisitos**  

Asegúrate de tener instaladas las siguientes herramientas:

- **Python >= 3.x**
- Librerías necesarias (pueden incluir `requests` y `pytest`)
- Archivo `sender_stand_request.py` para manejar solicitudes HTTP.
- Archivo `data.py` que contiene un diccionario con la estructura base del cuerpo de la solicitud y headers para las requests.

---

## ⚙️ **Estructura del Proyecto**  

```
📂 proyecto
│-- sender_stand_request.py  # Módulo que envía solicitudes HTTP
│-- data.py                  # Diccionario de datos para solicitudes
│-- test_user_creation.py    # Archivo principal con pruebas automatizadas
│-- README.md                # Documentación
```

---

## 🔧 **Instalación y Configuración**  

1. Clona el repositorio:  
   ```bash
   git clone https://github.com/quserforgitp/api_stand_tests.git
   cd api_stand_tests
   ```

---

## 🚦 **Casos de Prueba**  

| **Prueba**                               | **Descripción**                                                                 | **Resultado Esperado**           |
|------------------------------------------|--------------------------------------------------------------------------------|---------------------------------|
| `test_create_user_2_letter_in_first_name_get_success_response`  | El nombre tiene 2 caracteres.                                                   | Respuesta exitosa (201).         |
| `test_create_user_15_letters_in_first_name_get_success_response`| El nombre tiene 15 caracteres.                                                  | Respuesta exitosa (201).         |
| `test_create_user_1_letter_in_first_name_get_error_response`    | El nombre tiene solo 1 carácter.                                                | Error 400.                       |
| `test_create_user_16_letter_in_first_name_get_error_response`   | El nombre tiene 16 caracteres.                                                  | Error 400.                       |
| `test_create_user_has_space_in_first_name_get_error_response`   | El nombre contiene espacios.                                                    | Error 400.                       |
| `test_create_user_has_special_symbol_in_first_name_get_error_response` | El nombre contiene símbolos especiales.                                         | Error 400.                       |
| `test_create_user_has_number_in_first_name_get_error_response`  | El nombre contiene números.                                                     | Error 400.                       |
| `test_create_user_no_first_name_get_error_response`             | El parámetro `firstName` no está presente.                                      | Error 400.                       |
| `test_create_user_number_type_first_name_get_error_response`    | El parámetro `firstName` tiene un valor de tipo numérico.                       | Error 400.                       |

---

## ▶️ **Ejecución de las Pruebas**  

Para ejecutar las pruebas, utiliza el siguiente comando:  

```bash
python -m pytest create_user_test.py
```

---

## 📚 **Explicación del Código**  

### **Funciones Principales**  

1. **`get_user_body(name)`**  
   Devuelve un cuerpo de solicitud modificado con el valor `firstName` proporcionado.

2. **`positive_assert(first_name)`**  
   Prueba un caso exitoso:  
   - Verifica que el código de estado sea **201**.  
   - Valida que `authToken` exista y tenga valor.  
   - Comprueba que el usuario existe en la base de datos.

3. **`negative_assert_symbol(first_name)`**  
   Prueba casos negativos:  
   - Verifica que el código de estado sea **400**.  
   - Valida que el mensaje de error coincida con el esperado.

4. **`negative_assert_no_firstname(user_body)`**  
   Valida que se retorne un error cuando falta el parámetro `firstName`.

---

## 💻 **Ejemplo de Uso**  

Aquí un ejemplo de una prueba exitosa:  

```python
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")
```

Y un ejemplo de una prueba negativa:  

```python
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",")
```

---

