from __future__ import print_function
from datetime import date, datetime, timedelta
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

tomorrow = datetime.now().date() + timedelta(days=1)
emp_no = cursor.lastrowid
add_employee = ("INSERT INTO employees "
               "(emp_no, first_name, last_name, hire_date, gender, birth_date) "
               "VALUES (%s, %s, %s, %s, %s, %s)")
data_employee = (emp_no, 'Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))
# Insert new employee
cursor.execute(add_employee, data_employee)

emp_no = cursor.lastrowid
add_salary = ("INSERT INTO salaries "
              "(emp_no, salary, from_date, to_date) "
              "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
data_salary = {
  'emp_no': emp_no,
  'salary': 50000,
  'from_date': tomorrow,
  'to_date': date(9999, 1, 1),
}
# Insert salary information

cursor.execute(add_salary, data_salary)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()