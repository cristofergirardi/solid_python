class NumberGenerator:
    _instance = None
    _current_number = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NumberGenerator, cls).__new__(cls)
        return cls._instance
    
    def get_next_number(self):
        self._current_number += 1
        return self._current_number
    
if __name__ == "__main__":
    generator1 = NumberGenerator()
    generator2 = NumberGenerator()

    print(f"generator1 ID: {id(generator1)}")
    print(f"generator2 ID: {id(generator2)}")

    print(generator1.get_next_number())  # Output: 1
    print(generator2.get_next_number())  # Output: 2

    print(f"generator1 ID after increment: {id(generator1)}")
    print(f"generator2 ID after increment: {id(generator2)}")
    print(generator1.get_next_number())  # Output: 3
    print(generator2.get_next_number())  # Output: 4
        