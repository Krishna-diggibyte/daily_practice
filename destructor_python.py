class MyClass:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")


obj = MyClass()
del obj  # Destructor called when object is deleted
