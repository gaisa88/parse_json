import json

class JSONLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        with open(self.filepath, encoding='utf-8-sig') as f:
            return json.load(f)