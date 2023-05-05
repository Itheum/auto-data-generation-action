import json

test_json = {"test2": "test2"}

output_file = open("output/test_file.json", "w")
output_file.truncate(0)
output_file.write(json.dumps(test_json, sort_keys=True, indent=4))
output_file.close()
