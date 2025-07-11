from loaders.json_loader import JSONLoader
from parsers.json_parser import JSONParser
from writers.csv_writer import CsvWriter


class JSONToExcelConverter:
    def __init__(self, json_path, excel_path):
        self.json_path = json_path
        self.excel_path = excel_path

    def run(self):
        loader = JSONLoader(self.json_path)
        data = loader.load()

        parser = JSONParser(data)
        df = parser.to_dataframe()

        writer = CsvWriter(df, self.excel_path)
        writer.save()
        print(f'✅ SCV saved to {self.excel_path}')



if __name__ == '__main__':
    converter = JSONToExcelConverter('data.json', 'output.csv')
    converter.run()