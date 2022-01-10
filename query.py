import datetime
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
cursor = cnx.cursor()

query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
    last_name, first_name, hire_date))

cursor.close()
cnx.close()