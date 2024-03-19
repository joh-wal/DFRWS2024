import blackboxprotobuf
import json

# Vi använder vår exempel Protocolbuffer
protobufFilePath = "exerciseFiles/exampleProtobuf"

# Öppnar filen och läser dess innehåll i bytes sparar i variabel
with open(protobufFilePath, "rb") as file:
    protobufFile = file.read()

# returnerar två dicts i en tuple. Den första är själva datan den andra är en gissning vilken typ av data det handlar om
decodedProtobuf = blackboxprotobuf.decode_message(protobufFile)

# För att lite snyggare printa ut dict nr2 där den gissar innehållet använder vi json
print(json.dumps(decodedProtobuf[1], indent=2))

# Printa ut själva dict:en med datan i
print(decodedProtobuf[0])

# När vi väl hittat vilken/vilka data som är intressanta kan vi printa ut just den.
# Vi får ett bytes objekt som innehåller en sträng som vi decodar med utf-8
print(decodedProtobuf[0]['2']['3']['2'].decode("utf-8"))

