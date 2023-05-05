import json

object = {"key": "value"}

output_file = open("output/data.json", "w")
output_file.truncate(0)
output_file.write(json.dumps(object))
output_file.close()
