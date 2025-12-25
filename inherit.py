class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.behaviour = "friendly"
    

    def speak(self):
        super().speak()
        print(f"{self.name} Barks but {self.behaviour} ")


#animal = Animal("Generic Animal")
#animal.speak()

dog = Dog()
dog.speak()