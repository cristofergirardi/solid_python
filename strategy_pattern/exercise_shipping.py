from abc import ABC, abstractmethod
from enum import Enum

class CarrierType(Enum):
    FEDEX = "FedEx"
    UPS = "UPS"
    DHL = "DHL"

# Step 1: Create the ShippingStrategy interface
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_shipping_cost(self, weight: float) -> float:
        pass

# Step 2: Implement the shipping strategies
class FedExShipping(ShippingStrategy):
    def calculate_shipping_cost(self, weight: float) -> float:
        return weight * 2.5
    
class UPSShipping(ShippingStrategy):
    def calculate_shipping_cost(self, weight: float) -> float:
        return weight * 3.0
    
class DHLShipping(ShippingStrategy):
    def calculate_shipping_cost(self, weight: float) -> float:
        return weight * 4.0

# Step 3: Implement the ShippingContext class
class ShippingContext:
    def __init__(self, strategy: ShippingStrategy):
        self.strategy = strategy

    def calculate_shipping_cost(self, weight: float) -> float:
        return self.strategy.calculate_shipping_cost(weight)

class ShippingFactory:
    @staticmethod
    def get_shipping_strategy(carrier: CarrierType) -> ShippingStrategy:
        if carrier == CarrierType.FEDEX:
            return FedExShipping()
        elif carrier == CarrierType.UPS:
            return UPSShipping()
        elif carrier == CarrierType.DHL:
            return DHLShipping()
        else:
            raise ValueError("Invalid carrier type")

# Step 4: Test your implementation
if __name__ == "__main__":
    print("Select a carrier for shipping:")
    print("1. FedEx")
    print("2. UPS")
    print("3. DHL")

    choice = int(input("Enter the number corresponding to your choice: "))
    weight = float(input("Enter the weight of the package (in pounds): "))

    if choice == 1:
        carrier = CarrierType.FEDEX
    elif choice == 2:
        carrier = CarrierType.UPS
    elif choice == 3:
        carrier = CarrierType.DHL
    else:
        print("Invalid choice!")
        exit(1)

    strategy = ShippingFactory.get_shipping_strategy(carrier)

    shipping_context = ShippingContext(strategy)
    shipping_cost = shipping_context.calculate_shipping_cost(weight)
    print(f"The shipping cost for {carrier.value} is ${shipping_cost:.2f}")