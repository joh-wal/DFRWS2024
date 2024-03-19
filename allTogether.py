import zipfile

import pathlib
import sqlite3
import gzip
import blackboxprotobuf

zipFilePath = "Magnet CTF 2022 iOS subset minimal.zip"
tempFolder = "temp"

fileNameToSearch = "NoteStore.sqlite"



with zipfile.ZipFile(zipFilePath, "r") as openZipFile:
    for fileName in openZipFile.namelist():
        if fileNameToSearch in fileName:
            print("NotesStore found:", fileName)
            localFileName = fileName.rsplit("/", 1)[-1]
            print("Saving file:", localFileName)
            with open(pathlib.Path(tempFolder, localFileName), "wb") as localFile:
                localFile.write(openZipFile.read(fileName))



sqliteDatabase = pathlib.Path(tempFolder, fileNameToSearch)
print("\nOpen database: ", sqliteDatabase)

sqliteConnection = sqlite3.connect(sqliteDatabase)
sqliteCursor = sqliteConnection.cursor()

sqliteQ = "SELECT ZDATA FROM ZICNOTEDATA;"
print("\nExecuting SQLite: ", sqliteQ)

sqliteCursor.execute(sqliteQ)

sqliteResult = sqliteCursor.fetchall()
print("\nsqLite result:")
print(sqliteResult)

sqliteBLOB = sqliteResult[0][0]
print("\nsqliteBLOB:")
print(sqliteBLOB)

decompressedBLOB = gzip.decompress(sqliteBLOB)
print("\nDecompressed BLOB (protobuf)")
print(decompressedBLOB)

decodedProtobufBLOB = blackboxprotobuf.decode_message(decompressedBLOB)
print("\nDecoded Protobuf:")
print(decodedProtobufBLOB)

print("\nText inside note:")
print(decodedProtobufBLOB[0]['2']['3']['2'].decode("utf-8"))

openZipFile.close()