import configuration
import requests
import data

url_get_docs = configuration.URL_SERVICE + configuration.DOC_PATH
url_get_logs = configuration.URL_SERVICE + configuration.LOG_MAIN_PATH
url_get_table = configuration.URL_SERVICE + configuration.USERS_TABLE_PATH
url_create_user = configuration.URL_SERVICE + configuration.CREATE_USER_PATH
url_search_kits_by_products_id = configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH

def get_docs():
    return requests.get(url=url_get_docs)

def get_logs():
    return requests.get(url=url_get_logs, params={"count":20})

def get_users_table():
    return requests.get(url=url_get_table)

def post_new_user(body):

    return requests.post(
        url=url_create_user,
        headers=data.headers,
        json=body
    )

def post_products_kits(body):
    return requests.post(
        url=url_search_kits_by_products_id,
        headers=data.headers,
        json=body
    )

# response_docs = get_docs()
# response_logs = get_logs()
# response_users_table = get_users_table()
# response_post_new_user = post_new_user(data.user_body)
response_kits_by_products = post_products_kits(data.product_ids)
print(response_kits_by_products.status_code)
print(response_kits_by_products.json())