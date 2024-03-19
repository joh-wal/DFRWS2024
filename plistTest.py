import plistlib
import biplist

path = "exerciseFiles/City Run.plist"

with open(path, "rb") as openFile:
    fileContens = openFile.read()

plist = plistlib.loads(fileContens)

#biplist solutions works only with binary plist
plist2  = biplist.readPlist(path)

print("Plist nycklar:")
print(plist.keys())

print(type(plist["Locations"]))

print(len(plist["Locations"]))

locationsList = plist["Locations"]

print(type(locationsList[0]))

print(locationsList[0][0:10])

plistInside = plistlib.loads(locationsList[0])

print(plistInside)

print("Latitude: ", plistInside['$objects'][1]['kCLLocationCodingKeyCoordinateLatitude'])
print("Longitude:", plistInside['$objects'][1]['kCLLocationCodingKeyCoordinateLongitude'])
print("Timestamp:", plistInside['$objects'][1]['kCLLocationCodingKeyTimestamp'])
