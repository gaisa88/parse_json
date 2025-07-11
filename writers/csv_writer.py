
class CsvWriter:
    def __init__(self, dataframe, output_path):
        self.dataframe = dataframe
        self.output_path = output_path

    def save(self):
        self.dataframe.to_csv(self.output_path, index=False)