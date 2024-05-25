# import db_credentials as creds

# Select all
def select_all(cursor, table):
    cursor.execute("SELECT * FROM " + table)
    return cursor.fetchall()