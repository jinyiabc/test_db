import mysql.connector
import config
cfg = config.Config('mysql.cfg')

config = {
  'user': cfg['user'],
  'password': cfg['password'],
  'host': cfg['host'],
  'database': 'employees',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx.close()

