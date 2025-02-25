
import configuration
import requests
import data



#Envío de una respuesta GET

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,params={"count":20})



#---------------------------------------------------------
# Recuperar informacion de la tabla de la base de datos
#Crea una función para obtener la información de la base de datos

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


#----------------------------------------------------
#En esta lección, practicarás el envío de solicitudes para crear un nuevo usuario o usuaria.

def post_new_user (body):      #body es un parametro de la funcion
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                json=body,
                headers=data.headers)

#---------------------------------------------------
#Escribe una solicitud POST para buscar los kits por sus productos:
# Main.Products → Kit search by products (Búsqueda de kits por productos).
def post_products_kits(product_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=product_ids,
                         headers=data.headers)



