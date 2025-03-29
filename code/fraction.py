import math 

class Fraction:
    def __init__(self, numerator, denominator):
        # Initialize the numerator and denominator properties
        # Check that the denominator is non-zero
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        # Add the current fraction and the other fraction
        # Return the result as a new Fraction object
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    
    def subtract(self, other):
        # Subtract the other fraction from the current fraction
        # Return the result as a new Fraction object
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def multiply(self, other):
        # Multiply the current fraction and the other fraction
        # Return the result as a new Fraction object
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def divide(self, other):
        # Divide the current fraction by the other fraction
        # Check that the other fraction has a non-zero numerator
        # Return the result as a new Fraction object
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
            
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def simplify(self):
        # Simplify the current fraction to its simplest form
        # Return a new Fraction object with the simplified numerator and denominator
        gcd = math.gcd(abs(self.numerator), abs(self.denominator))
        simplified_numerator = self.numerator // gcd
        simplified_denominator = self.denominator // gcd

        # Ensure the denominator is positive
        if simplified_denominator < 0:
            simplified_numerator *= -1
            simplified_denominator *= -1
            
        return Fraction(simplified_numerator, simplified_denominator)

    def __str__(self):
        # Return the string representation of the fraction in the format "numerator/denominator"
        return f'{self.numerator}/{self.denominator}'


# Test your implementation
fraction1 = Fraction(1, 4)
fraction2 = Fraction(1, 2)

fraction3 = fraction1.add(fraction2)
print(fraction3)  # Should output "6/8"

fraction4 = fraction3.simplify()
print(fraction4)  # Should output "3/4"
