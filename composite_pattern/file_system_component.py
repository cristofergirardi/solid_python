from abc import ABC, abstractmethod

# Define an abstract base class for all file system components
class FileSystemComponent(ABC):
    def __init__(self, name):
        # Constructor to initialize the common name attribute for any file system component
        self.name = name

    @abstractmethod
    def display(self):
        """Display information about the component. Must be implemented by all subclasses."""
        pass

    @abstractmethod
    def get_size(self):
        """Return the size of the component in bytes. Must be implemented by all subclasses."""
        pass

# Define the File class that represents a file in the file system
class File(FileSystemComponent):
    def __init__(self, name, size):
        # Initialize the base class with the name
        super().__init__(name)
        # File size is specific to the File class
        self.size = size

    def display(self):
        # Print details about the file, including its name and size
        print(f"File: {self.name}, Size: {self.size} bytes")

    def get_size(self):
        # Return the size of the file
        return self.size

# Define the Directory class that represents a directory in the file system
class Directory(FileSystemComponent):
    def __init__(self, name):
        # Initialize the base class with the name
        super().__init__(name)
        # A directory has a list of children that can be files or other directories
        self.children = []

    def add(self, component):
        # Add a file or directory to the directory's list of children
        self.children.append(component)

    def remove(self, component):
        # Remove a file or directory from the directory's list of children
        self.children = [child for child in self.children if child != component]

    def display(self):
        # Display information about the directory itself
        print(f"Directory: {self.name}")
        # Recursively display information about each child in the directory
        for child in self.children:
            child.display()

    def get_size(self):
        # Calculate the total size of the directory by summing the sizes of its contents
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size

    def list_files(self):
        # List all the files contained in this Directory instance
        files = []
        for child in self.children:
            if isinstance(child, File):
                files.append(child.name) # Add the name of the file
            elif isinstance(child, Directory):
                files.extend(child.list_files())
        return files

# Usage
file1 = File("file1.txt", 1200)  # size in bytes
file2 = File("file2.txt", 1500)  # size in bytes
file3 = File("file3.txt", 1000)  # size in bytes
dir1 = Directory("dir1")
dir2 = Directory("dir2")

dir1.add(file1)
dir1.add(file2)
dir2.add(file3)
dir1.add(dir2)

print("Before removal:")
dir1.display()

# Display total size of dir1
print(f"Total size of {dir1.name} before removal: {dir1.get_size()} bytes")

# List all files in dir1
print("\nListing all files in dir1:")
print(dir1.list_files())

# Remove file2 and dir2
dir1.remove(file2)
dir1.remove(dir2)

print("\nAfter removal:")
dir1.display()

# List all files in dir1
print("\nListing all files in dir1:")
print(dir1.list_files())

# Display total size of dir1
print(f"Total size of {dir1.name}: {dir1.get_size()} bytes")

