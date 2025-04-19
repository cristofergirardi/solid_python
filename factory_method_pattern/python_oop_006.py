from abc import ABC, abstractmethod
from typing import Type

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

class NotImplementingInterface:
    def some_method(self):
        print("I am not implementing MyInterface")

def process_my_interface(obj: MyInterface):
    obj.my_method()
    print("The object has correctly implemented MyInterface")

# Testing the implementation
my_obj = MyClass()
process_my_interface(my_obj)

another_obj = AnotherClass()
process_my_interface(another_obj)

# This will not raise a runtime error, but static type checkers like mypy will complain
not_implementing_interface = NotImplementingInterface()
process_my_interface(not_implementing_interface)  # Static type checkers will warn about this