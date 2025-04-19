from abc import ABC, abstractmethod
from enum import Enum
 
# Step 0: Create an enumeration for vehicle types
# Enum to define different types of vehicles.
class VehicleType(Enum):
    CAR = "Car"
    MOTORCYCLE = "Motorcycle"
    BICYCLE = "Bicycle"
 
# Step 1: Create an abstract Vehicle class
# Abstract class that defines the structure for all vehicles.
class Vehicle(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass
 
# Step 2: Create concrete vehicle classes
# Concrete vehicle classes that implement the Vehicle interface.
class Car(Vehicle):
    def get_name(self) -> str:
        return "Car"
 
class Motorcycle(Vehicle):
    def get_name(self) -> str:
        return "Motorcycle"
 
class Bicycle(Vehicle):
    def get_name(self) -> str:
        return "Bicycle"
 
# Step 3: Create a VehicleFactory class
class VehicleFactory:
    def create_vehicle(self, vehicle_type: VehicleType) -> Vehicle:
        if vehicle_type == VehicleType.CAR:
            return Car()
        elif vehicle_type == VehicleType.MOTORCYCLE:
            return Motorcycle()
        elif vehicle_type == VehicleType.BICYCLE:
            return Bicycle()
        else:
            raise ValueError(f"Invalid vehicle type: {vehicle_type}")
 
# Step 4: Test the VehicleFactory class
def main():
    vehicle_factory = VehicleFactory()
 
    car = vehicle_factory.create_vehicle(VehicleType.CAR)
    print(car.get_name())
 
    motorcycle = vehicle_factory.create_vehicle(VehicleType.MOTORCYCLE)
    print(motorcycle.get_name())
 
    bicycle = vehicle_factory.create_vehicle(VehicleType.BICYCLE)
    print(bicycle.get_name())
 
if __name__ == "__main__":
    main()