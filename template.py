import mysql.connector
from helper.configSQL import config

cnx = mysql.connector.connect(**config)

cnx.close()

