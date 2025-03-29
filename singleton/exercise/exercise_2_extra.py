import threading

class NumberGenerator:
    _instance = None
    _lock = threading.Lock()
    _current_number = 0

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(NumberGenerator, cls).__new__(cls)
        return cls._instance
    
    def get_next_number(self):
        with self._lock:
            # Increment the current number in a thread-safe manner
            self._current_number += 1
        return self._current_number
    
def test_singleton_thread_safe():
    generator = NumberGenerator()
    # print(f"Generator ID: {id(generator)}")
    print(f"Generated Number: {generator.get_next_number()}")

if __name__ == "__main__":
    threads_list = []
    for _ in range(100):
        thread = threading.Thread(target=test_singleton_thread_safe)
        threads_list.append(thread)
        thread.start()

    for thread in threads_list:
        thread.join()
       