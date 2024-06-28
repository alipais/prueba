# Configuración de la base de datos
import mysql.connector

config_dev = {
    # configuración en desarrollo (local)
    "user": 'Alipais',
    'password': 'grupo102024',
    'host': 'https://alipais.pythonanywhere.com/api/usuarios',
    'database': 'Alipais$favorite_cake'
}

config_prod = {
    # configuración en producción (despliegue)
    "user": '',
    'password': '',
    'host': '',
    'database': ''
}

conexion = mysql.connector.connect(**config_dev)