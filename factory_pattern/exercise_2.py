from abc import ABC, abstractmethod
from enum import Enum

# Step 0: Create an enumeration for animal types
class AnimalType(Enum):
    DOG = "Dog"
    CAT = "Cat"
    FISH = "Fish"

# Step 1: Create an abstract Animal class
class Animal(ABC):
    @abstractmethod
    def get_info(self) -> str:
        pass

# Step 2: Create concrete animal classes
class Dog(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def get_info(self) -> str:
        return "Dog"    
    

class Cat(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name

    def get_info(self) -> str:
        return "Cat"

class Fish(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name

    def get_info(self) -> str:
        return "Fish"

# Step 3: Create an AnimalFactory class
class AnimalFactory:
    def create_animal(self, animal_type: AnimalType, context: dict) -> Animal:
        # Implement the logic to create an animal based on the animal_type parameter and context data
        if animal_type == AnimalType.DOG:
            return Dog(context["name"], context["age"])
        elif animal_type == AnimalType.CAT:
            return Cat(context["name"], context["age"])
        elif animal_type == AnimalType.FISH:
            return Fish(context["name"], context["age"])
        else:
            raise ValueError(f"Invalid animal type: {animal_type}")

# Step 4: Test the AnimalFactory class
def main():
    animal_factory = AnimalFactory()

    # Test the AnimalFactory by creating different types of animals and passing context data
    dog = animal_factory.create_animal(AnimalType.DOG, {"name": "Buddy", "age": 3})
    print(dog.get_info())
    cat = animal_factory.create_animal(AnimalType.CAT, {"name": "Whiskers", "age": 2})
    print(cat.get_info())
    fish = animal_factory.create_animal(AnimalType.FISH, {"name": "Nemo", "age": 1})
    print(fish.get_info())
    

if __name__ == "__main__":
    main()
