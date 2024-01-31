import sqlite3


def create_table_if_not_exists():
    connection = sqlite3.connect('licenseplates.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS license_plates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            license_plate TEXT UNIQUE
        )
    ''')
    connection.commit()
    connection.close()


def store_license_plates(license_plates):
    connection = sqlite3.connect('licenseplates.db')
    cursor = connection.cursor()
    for plate in license_plates:
        try:
            cursor.execute(
                'INSERT INTO license_plates (license_plate) VALUES (?)', (plate,))
        except sqlite3.IntegrityError:
            pass
    connection.commit()
    connection.close()


def read_license_plates():
    connection = sqlite3.connect('licenseplates.db')
    cursor = connection.cursor()
    cursor.execute('SELECT license_plate FROM license_plates')
    rows = cursor.fetchall()
    connection.close()
    return [row[0] for row in rows]


license_plates_list = ["ABC123", "XYZ789", "DEF456", "ABC123", "GHI789"]

create_table_if_not_exists()
store_license_plates(license_plates_list)
