import blackboxprotobuf
import json

protobufFilePath = "exerciseFiles/exampleProtobuf"

with open(protobufFilePath, "rb") as file:
    protobufFile = file.read()

decodedProtobuf = blackboxprotobuf.decode_message(protobufFile)

print(json.dumps(decodedProtobuf[1], indent=2))

print(decodedProtobuf[0])

print(decodedProtobuf[0]['2']['3']['2'].decode("utf-8"))

