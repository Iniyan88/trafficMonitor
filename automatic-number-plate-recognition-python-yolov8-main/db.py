import mysql.connector
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = ''
MYSQL_HOST = 'localhost'
MYSQL_DATABASE = '5g_contest'


def create_table_if_not_exists(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS noofcars (
            id INT AUTO_INCREMENT PRIMARY KEY,
            PIN VARCHAR(20))
    ''')


def store_license_plates(license_plates):
    connection = mysql.connector.connect(
        user=MYSQL_USERNAME,
        password=MYSQL_PASSWORD,
        host=MYSQL_HOST,
        database=MYSQL_DATABASE,
        port=3308
    )
    cursor = connection.cursor()

    create_table_if_not_exists(cursor)

    for plate in license_plates:
        try:
            cursor.execute(
                'INSERT INTO noofcars (PIN) VALUES (%s)', (plate,))
            connection.commit()
        except mysql.connector.IntegrityError:
            pass

    connection.close()


def read_license_plates():
    connection = mysql.connector.connect(
        user=MYSQL_USERNAME,
        password=MYSQL_PASSWORD,
        host=MYSQL_HOST,
        database=MYSQL_DATABASE,
        port=3308
    )
    cursor = connection.cursor()

    cursor.execute('SELECT PIN FROM noofcars')
    rows = cursor.fetchall()

    connection.close()

    return [row[0] for row in rows]


if __name__ == "__main__":
    license_plates_list = ["ABC123", "XYZ789", "DEF456", "ABC123", "GHI789"]

    store_license_plates(license_plates_list)
    stored_license_plates = read_license_plates()
    print(stored_license_plates)
