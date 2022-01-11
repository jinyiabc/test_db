import mysql.connector
from mysql.connector import errorcode

from helper.configSQL import config

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

DB_NAME = 'china_stock_wiki'
TABLES = {}
TABLES['china_stock_wiki'] = (
    "CREATE TABLE `china_stock_wiki` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'UTF8MB4'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

# Test for database exists
try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
    # Create database if not exists.
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        # define database name.
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

# for table_name in TABLES:
#     table_description = TABLES[table_name]
#     try:
#         print("Creating table {}: ".format(table_name), end='')
#         cursor.execute(table_description)
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#             print("already exists.")
#         else:
#             print(err.msg)
#     else:
#         print("OK")

cursor.close()

cnx.close()

