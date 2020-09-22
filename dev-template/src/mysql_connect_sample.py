import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'user',
    'password': 'password',
    'host': 'mysql_container',
    'database': 'sample_db',
    'port': '3306',
}

if __name__ == "__main__":
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute('select * from users')
        for row in cursor.fetchall():
            print("name:" + str(row[0]) + "" + "time_zone_id" + str(row[1]))
        conn.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        conn.close()
