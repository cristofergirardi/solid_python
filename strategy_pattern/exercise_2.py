from abc import ABC, abstractmethod
from typing import List, Dict, Any
import csv

# Step 1: Create the FileParser interface
class FileParser(ABC):

    @abstractmethod
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        pass

# Step 2: Implement the file parsers
# TODO: Implement CSVParser, JSONParser, and XMLParser classes
class CSVParser(FileParser):
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:        
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

class JSONParser(FileParser):
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        import json
        with open(file_path, mode='r') as file:
            return json.load(file)
        
class XMLParser(FileParser):
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        import xml.etree.ElementTree as ET
        tree = ET.parse(file_path)
        root = tree.getroot()
        data = []
        for elem in root:
            data.append({child.tag: child.text for child in elem})
        return data
            
# Step 3: Implement the FileReader class
class FileReader:

    def __init__(self, file_parser: FileParser):
        # TODO: Initialize the file reader with the given file_parser
        self.file_parser = file_parser

    def read_file(self, file_path: str) -> List[Dict[str, Any]]:
        # TODO: Read the file at the given file_path and return a list of dictionaries using the specified file parser
        return self.file_parser.parse_file(file_path)

# Step 4: Test your implementation
if __name__ == "__main__":
    # TODO: Create a file reader with a CSVParser
    reader = FileReader(CSVParser())

    # TODO: Read a sample CSV file and print the list of dictionaries
    data = reader.read_file("sample.csv")
    print(data)
