class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        return "Unknown sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__("Dog")
        self.name = name
        self.breed = breed

    def sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__("Cat")
        self.name = name
        self.breed = breed

    def sound(self):
        return "Meow!"

dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers", "Siamese")

print(dog.species)
print(cat.name)
print(cat.sound())
