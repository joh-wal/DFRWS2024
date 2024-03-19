import plistlib
import NSKeyedUnArchiver


path = "exerciseFiles/currentWidgetReadingHistoryData.plist"

with open(path, "rb") as openFile:
    rawPlist = openFile.read()

plist = plistlib.loads(rawPlist)

print(plist)

archive = NSKeyedUnArchiver.unserializeNSKeyedArchiver(rawPlist)

print(archive)