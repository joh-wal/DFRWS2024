import sqlite3

# Vi behöver självklart en databas - i den här fallet historik-databasen från Firefox
sqliteDatabase = "exerciseFiles/places.sqlite"

# Vi vet redan på förhand vilken sqlite-fråga som får ut det mest intressanta från databasen, vi sparar ner den till en variabel
sqliteQHistory = "SELECT url, title, datetime(visit_date/1000000,'unixepoch') AS TimeStamp FROM moz_historyvisits, moz_places WHERE moz_historyvisits.place_id = moz_places.id;"

# Först behöver vi en uppkoppling mot databasen
sqliteConnection = sqlite3.connect(sqliteDatabase)

# Sen behöver vi en "pekare" för att kunna interagera med databasen
sqliteCursor = sqliteConnection.cursor()

# Med hjälp av pekaren kan vi skicka in vår fråga till databasen
sqliteCursor.execute(sqliteQHistory)

# Vi kan även hämta resultatet av vår nyss ställda fråga genom pekaren
sqliteResult = sqliteCursor.fetchall()

# Vi får tillbaka en lista med tuples (en tuple för varje rad i svaret)
# Vi itererar över listan och skriver ut tuples
for row in sqliteResult:
    print(row)

# Stänger databasen
sqliteConnection.close()