import sqlite3

def getSqliteQueryFromDataBase(query, databasePath):
    sqliteConnection = sqlite3.connect(databasePath)
    sqliteCursor = sqliteConnection.cursor()
    sqliteCursor.execute(query)
    result = sqliteCursor.fetchall()
    sqliteConnection.close()
    return result