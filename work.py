import json

class JSONWorker:
    def __init__(self, data):
        if not isinstance(data, list) or len(data) != 3:
            raise ValueError("Data should be a list with 3 dictionaries")
        for item in data:
            if not isinstance(item, dict) or len(item) != 2:
                raise ValueError("Each dictionary should have exactly 2 key-value pairs")
        self.data = data

    def write_to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def read_from_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

data = [
    {"key1": "value1", "key2": "value2"},
    {"key3": "value3", "key4": "value4"},
    {"key5": "value5", "key6": "value6"}
]

worker = JSONWorker(data)
worker.write_to_json('data.json')

read_data = worker.read_from_json('data.json')
print(read_data)