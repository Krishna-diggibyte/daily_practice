# Define a class
class Dog:
    # Constructor method
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # Method to bark
    def bark(self):
        return "Woof!"

# Create objects (instances) of the Dog class
dog1 = Dog("Buddy", "Labrador")
dog2 = Dog("Max", "Poodle")

# Access object attributes and call methods
print(dog1.name)
print(dog2.breed)
print(dog1.bark())