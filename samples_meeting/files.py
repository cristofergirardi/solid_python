from abc import ABC, abstractmethod

class FilesAbstract(ABC):
    def __init__(self, filename: str):
        self.filename = filename
        
class Files(FilesAbstract):
    def __init__(self, filename: str):
        super().__init__(filename)
        
    @abstractmethod
    def check_file(self):
        pass

class FilesGeral(Files):
    def check_file(self):
        print(f"Checking general file: {self.filename}")    
    
class FilesCSV(FilesGeral):
    def has_file(self):
        return True

class FilesJSON(FilesGeral):
    def has_file(self):
        return False

class RunFiles:
    def validate_files(self, files: Files):
        files.check_file()
        print(f"There is file: {files.has_file()}")
                

if __name__ == "__main__":
    run_files = RunFiles()
    
    filesCSV = FilesCSV("data.csv")
    run_files.validate_files(filesCSV)
    
    filesJSON = FilesJSON("data.json")
    run_files.validate_files(filesJSON)


