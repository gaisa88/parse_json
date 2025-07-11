import pandas as pd

class JSONParser:
    def __init__(self, data):
        self.data = data

    def to_dataframe(self):
        if isinstance(self.data, list):
            return pd.DataFrame(self.data)
        elif isinstance(self.data, dict):
            return pd.DataFrame([self.data])
        else:
            raise ValueError("Unsupported JSON structure")