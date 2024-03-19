import sqlite3

sqliteDatabase = "exerciseFiles/places.sqlite"

sqliteQHistory = "SELECT url, title, datetime(visit_date/1000000,'unixepoch') AS TimeStamp FROM moz_historyvisits, moz_places WHERE moz_historyvisits.place_id = moz_places.id;"

sqliteConnection = sqlite3.connect(sqliteDatabase)

sqliteCursor = sqliteConnection.cursor()

sqliteCursor.execute(sqliteQHistory)

sqliteResult = sqliteCursor.fetchall()

for row in sqliteResult:
    print(row)

sqliteConnection.close()
