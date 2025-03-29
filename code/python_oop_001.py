# Define the Greeting class
class Greeting:
    # Constructor for the Greeting class
    def __init__(self, name):
        # Initialize the 'name' attribute with the provided value
        self.name = name

    # Define the 'say_hello' method for the Greeting class
    def say_hello(self):
        # Print a personalized greeting message using the 'name' attribute
        print(f"Hello, {self.name}!")

class BetterGreeting(Greeting) :
    def say_hello(self):
        super().say_hello()
        print(f"Hello, Better {self.name}!")

# Create an object of the Greeting class, initializing it with the name 'John'
greeting = BetterGreeting("John")

# Call the 'say_hello' method on the 'greeting' object to print the greeting message
greeting.say_hello()
