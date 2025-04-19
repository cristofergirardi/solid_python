from abc import ABC, abstractmethod
from enum import Enum

class ProcessEnum(Enum):
    UPPER = "upper"
    LOWER = "lower"
    CAP = "cap"

class TextProcessingStrategy(ABC):
    @abstractmethod
    def process_text(self, text: str) -> str:
        pass

class UpperCaseStrategy(TextProcessingStrategy):
    def process_text(self, text: str) -> str:
        return text.upper()
    
class LowerCaseStrategy(TextProcessingStrategy):   
    def process_text(self, text: str) -> str:
        return text.lower()
    
class CapitalizeStrategy(TextProcessingStrategy):
    def process_text(self, text: str) -> str:
        return text.capitalize()
    
class RegularStrategy(TextProcessingStrategy):
    def process_text(self, text: str) -> str:
        return text
    
class TextProcessingContext:
    def __init__(self, strategy: TextProcessingStrategy):
        self.strategy = strategy

    def process_text(self, text: str) -> str:
        return self.strategy.process_text(text)
    
class TextProcessingFactory:
    @staticmethod
    def get_text_processing_strategy(process: ProcessEnum) -> TextProcessingStrategy:
        if process == ProcessEnum.UPPER.value:
            return UpperCaseStrategy()
        elif process == ProcessEnum.LOWER.value:
            return LowerCaseStrategy()
        elif process == ProcessEnum.CAP.value:
            return CapitalizeStrategy()
        else:
            return RegularStrategy()
        
if __name__ == "__main__":
    print("Select a text processing operation:")
    print("upper")
    print("lower")
    print("cap")
    print("regular")

    operation = input("Choise one: ")
    input_text = input("Enter the text to process: ")

    strategy = TextProcessingFactory.get_text_processing_strategy(operation)
    context = TextProcessingContext(strategy)
    
    output_text = context.process_text(input_text)
    print(output_text)