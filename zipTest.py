import zipfile

zipFilePath = "exerciseFiles/test.zip"

with zipfile.ZipFile(zipFilePath, "r") as openZipFile:
    for file in openZipFile.namelist():
        print(file)


with zipfile.ZipFile(zipFilePath, "r") as openZipFile:
    for file in openZipFile.namelist():
        if "bingo" in file:
            fileContents = openZipFile.read(file)
            print(fileContents)

