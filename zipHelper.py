import zipfile

def fileDumper(filePath, zipFilePath, dest="./"):
    with zipfile.ZipFile(zipFilePath, "r") as openZipFile:
        for file in openZipFile.namelist():
            if file == filePath:
                print("Dumping", file, "to", dest, ".")
                openZipFile.extract(file, dest)


def fileReader(filePath, zipFilePath):
    with zipfile.ZipFile(zipFilePath, "r") as openZipFile:
        for file in openZipFile.namelist():
            if file == filePath:
                return openZipFile.read(filePath)


def pathDumper(filePath, zipFilePath, dest="./"):
    with zipfile.ZipFile(zipFilePath, "r") as openZipFile:
        for file in openZipFile.namelist():
                if file.startswith(filePath):
                    print("Dumping", file, "to", dest, ".")
                    openZipFile.extract(file, dest)