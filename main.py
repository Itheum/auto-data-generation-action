import json

test_json = {"test1": "test1"}

output_file = open("output/test_file.json", "a")
output_file.truncate(0)
output_file.write(json.dumps(test_json, sort_keys=True, indent=4))
output_file.close()
