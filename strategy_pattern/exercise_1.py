from abc import ABC, abstractmethod

# Step 1: Create the DiscountStrategy interface
class DiscountStrategy(ABC):

    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass

# Step 2: Implement the discount strategies
# TODO: Implement NoDiscount, PercentageDiscount, and FixedAmountDiscount classes
class NoDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total
    
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, total: float) -> float:
        return total * (1 - self.percentage / 100)
    
class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount

    def apply_discount(self, total: float) -> float:
        return max(0, total - self.amount)

# Step 3: Implement the ShoppingCart class
class ShoppingCart:

    def __init__(self, discount_strategy):
        # TODO: Initialize the shopping cart with the given discount_strategy and an empty items dictionary
        self.discount_strategy = discount_strategy
        self.items = {}

    def add_item(self, item: str, price: float):
        # TODO: Add the item with its price to the items dictionary
        if item in self.items:
            self.items[item] += price
        else:
            self.items[item] = price

    def remove_item(self, item: str):
        # TODO: Remove the item from the items dictionary if it exists
        if item in self.items:
            del self.items[item]

    def get_total(self) -> float:
        # TODO: Calculate and return the total price of the items in the cart
        return sum(self.items.values())

    def get_total_after_discount(self) -> float:
        # TODO: Calculate and return the total price of the items in the cart after applying the discount
        total = self.get_total()
        return self.discount_strategy.apply_discount(total)

# Step 4: Test your implementation
if __name__ == "__main__":
    # TODO: Create a shopping cart with a discount strategy
    cart = ShoppingCart(PercentageDiscount(10))

    # TODO: Add a few items
    cart.add_item("Item 1", 10.0)
    cart.add_item("Item 2", 20.0)
    cart.add_item("Item 3", 30.0)

    # TODO: Calculate and print the total price before discount
    print("Total before discount:", cart.get_total())

    # TODO: Calculate and print the total price after applying the discount
    print("Total after discount:", cart.get_total_after_discount())
