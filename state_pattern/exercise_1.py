from abc import ABC, abstractmethod

# Step 1: Define the abstract base class TicketState
class TicketState(ABC):

    @abstractmethod
    def assign(self, ticket):
        pass

    @abstractmethod
    def resolve(self, ticket):
        pass

    @abstractmethod
    def close(self, ticket):
        pass

# Step 2: Implement the concrete state classes
class NewState(TicketState):

    def assign(self, ticket):
        # Implement the behavior for assigning a new ticket
        ticket.state = AssignedState()
        print("Ticket has been assigned.")

    def resolve(self, ticket):
        # Implement the behavior for resolving a new ticket
        print("Cannot resolve a new ticket. Assign it first.")

    def close(self, ticket):
        # Implement the behavior for closing a new ticket
        ticket.state = ClosedState()
        print("Ticket has been closed.")

# Implement the other concrete state classes: AssignedState, ResolvedState, and ClosedState
class AssignedState(TicketState):
    def assign(self, ticket):
        # Implement the behavior for assigning an assigned ticket
        print("Ticket is already assigned.")

    def resolve(self, ticket):
        # Implement the behavior for resolving an assigned ticket
        ticket.state = ResolvedState()
        print("Ticket has been resolved.")

    def close(self, ticket):
        # Implement the behavior for closing an assigned ticket
        ticket.state = ClosedState()
        print("Ticket has been closed.")

class ResolvedState(TicketState):
    def assign(self, ticket):
        # Implement the behavior for assigning a resolved ticket
        print("Cannot assign a resolved ticket.")

    def resolve(self, ticket):
        # Implement the behavior for resolving a resolved ticket
        print("Ticket is already resolved.")

    def close(self, ticket):
        # Implement the behavior for closing a resolved ticket
        ticket.state = ClosedState()
        print("Ticket has been closed.")

class ClosedState(TicketState):
    def assign(self, ticket):
        # Implement the behavior for assigning a closed ticket
        print("Cannot assign a closed ticket.")

    def resolve(self, ticket):
        # Implement the behavior for resolving a closed ticket
        print("Cannot resolve a closed ticket.")

    def close(self, ticket):
        # Implement the behavior for closing a closed ticket
        print("Ticket is already closed.")    

# Step 3: Implement the Ticket class
class Ticket:

    def __init__(self):
        # Initialize the ticket's state attribute with an instance of the NewState class
        self.state = NewState()

    def assign(self):
        # Delegate the assign method call to the current state object
        self.state.assign(self)

    def resolve(self):
        # Delegate the resolve method call to the current state object
        self.state.resolve(self)

    def close(self):
        # Delegate the close method call to the current state object
        self.state.close(self)

# Step 4: Test the behavior of the ticket and its state transitions
def main():
    ticket = Ticket()

    # Test the initial state and transitions
    ticket.assign()
    ticket.resolve()
    ticket.close()

    # Test invalid transitions
    ticket.assign()
    ticket.resolve()

if __name__ == "__main__":
    main()
