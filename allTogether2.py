import zipfile
import pathlib
import sqlite3
import biplist
import NSKeyedUnArchiver
from tabulate import tabulate

zipFilePath = "Magnet CTF 2022 iOS subset minimal.zip"

tempFolder = "temp"

fileNameToSearch = "applicationState.db"


with zipfile.ZipFile(zipFilePath, "r") as openZipFile:
    for fileName in openZipFile.namelist():
        if fileNameToSearch in fileName:
            localFileName = fileName.rsplit("/", 1)[-1]
            print("Saving file:", localFileName)
            with open(pathlib.Path(tempFolder, localFileName), "wb") as localFile:
                localFile.write(openZipFile.read(fileName))


sqliteDatabase = pathlib.Path(tempFolder, fileNameToSearch)
print("\nOpen database: ", sqliteDatabase)

sqliteConnection = sqlite3.connect(sqliteDatabase)
sqliteCursor = sqliteConnection.cursor()

sqliteQ ="select application_identifier_tab.application_identifier, kvs.value from kvs, key_tab,application_identifier_tab where key_tab.key='compatibilityInfo' and kvs.key = key_tab.id and application_identifier_tab.id = kvs.application_identifier order by application_identifier_tab.id;"


sqliteCursor.execute(sqliteQ)
sqliteResult2 = sqliteCursor.fetchall()
listApps = []
for row in sqliteResult2:
    #print(row)
    bundleId = row[0]
    plist1 = biplist.readPlistFromString(row[1])
    #plist2 = biplist.readPlistFromString(plist1)
    print(plist1)
    #print(plist2)
    #print(plist2["$objects"][4])
    archive = NSKeyedUnArchiver.unserializeNSKeyedArchiver(plist1)
    #print(archive)
    print("App Bundle Name:", archive["bundlePath"].rsplit("/", 1)[1], " SandBox Path: ", archive["sandboxPath"], "Bundle Identifier: ", archive["bundleIdentifier"])
    appInfo = []
    appInfo.append(archive["bundlePath"].rsplit("/", 1)[1])
    appInfo.append(archive["sandboxPath"])
    appInfo.append(archive["bundleIdentifier"])
    listApps.append(appInfo)

print(tabulate(listApps, headers=["App Name", " Sandbox Path", "BundleID"]))
openZipFile.close()