from abc import ABC, abstractmethod

class MyInterface(ABC):
    @abstractmethod
    def my_method(self):
        pass

class MyClass(MyInterface):
    def my_method(self):
       print("my_method implementation in MyClass")

class AnotherClass(MyInterface):
    def my_method(self):
        print("my_method implementation in AnotherClass")

# Testing the implementation
my_obj = MyClass()
my_obj.my_method()

another_obj = AnotherClass()
another_obj.my_method()
