import plistlib
import biplist

path = "exerciseFiles/City Run.plist"

with open(path, "rb") as openFile:
    fileContens = openFile.read()

plist = plistlib.loads(fileContens)

#biplist solutions works only with binary plist
plist2  = biplist.readPlist(path)

# Skriver ut "root"-nycklarna i vår plist
print("Plist nycklar:")
print(plist.keys())

# Vad är Locations för något?
print(type(plist["Locations"]))

# Hur många entries har vi i listan?
print(len(plist["Locations"]))

# Sparar listan Locatoins till en variabel
locationsList = plist["Locations"]

# Vad har vi först i listan?
print(type(locationsList[0]))

# Tittar på de första bytes:en i datan:
print(locationsList[0][0:10])

# AHA! Ännu en plist - Konverterar till en dict och parar den till en variabel:
plistInside = plistlib.loads(locationsList[0])

# Skriver ut hela dictionaryn
print(plistInside)

# Skriver ut intressant data från dict i en lista
# Tar värdet från key:n X i dicten på position 1 i listan som finns som value på key:n $objects
print("Latitude: ", plistInside['$objects'][1]['kCLLocationCodingKeyCoordinateLatitude'])
print("Longitude:", plistInside['$objects'][1]['kCLLocationCodingKeyCoordinateLongitude'])
print("Timestamp:", plistInside['$objects'][1]['kCLLocationCodingKeyTimestamp'])