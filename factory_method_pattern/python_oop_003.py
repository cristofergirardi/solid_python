from abc import ABC, abstractmethod

# Define an abstract class 'Animal'
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    # Make the 'description' method abstract but provide a basic implementation
    def description(self):
        print(f"{self.__class__.__name__} says: {self.sound()}")

# Define a concrete class 'Dog' that inherits from 'Animal'
class Dog(Animal):
    def sound(self):
        return "Woof!"
    
    def description(self):
        print(f"My little dog says: {self.sound()}")

# Define a concrete class 'Cat' that inherits from 'Animal'
class Cat(Animal):
    def sound(self):
        return "Meow!"

# Create instances of concrete classes and use the overridden 'description' method
dog = Dog()
dog.description()

cat = Cat()
cat.description()