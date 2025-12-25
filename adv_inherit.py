# Single Inheritance
# =====================================================

# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def intro(self):
#         print(f"Hello, my name is {self.name}")

# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing")


# child = Child("Tommy")
# child.play()

# =====================================================

# Multilevel Inheritance
# =====================================================

# class GrandFather:
#     def __init__(self, name):
#         self.name = name
    
#     def tell_story(self):
#         print(f"{self.name} tells a story")

# class Father(GrandFather):
#     def work(self):
#         print(f"{self.name} is working")

# class Son(Father):
#     def study(self):
#         print(f"{self.name} is studying")

# son = Son("John")
# son.tell_story()
# son.work()
# son.study()

# =====================================================

# Hierarchical Inheritance
# =====================================================

# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def intro(self):
#         print(f"Hello, my name is {self.name}")

# class Child1(Parent):
#     def play(self):
#         print(f"{self.name} is playing")

# class Child2(Parent):
#     def study(self):
#         print(f"{self.name} is studying")

# child1 = Child1("Tommy")
# child2 = Child2("Jimmy")

# child1.intro()
# child1.play()

# child2.intro()
# child2.study()

# =====================================================

# Multiple Inheritance
# =====================================================

# class A:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello from class A, {self.name} ")

# class B(A):
#     def greet(self):
#         super().greet()
#         print(f"Hello from class B, {self.name} ")

# class C(A):
#     def greet(self):
#         super().greet()
#         print(f"Hello from class C, {self.name} ")

# class D(B, C):
#     def greet(self):
#         super().greet()
#         print(f"Hello from class D, {self.name} ")

# d = D("Alice")
# d.greet()

# =====================================================

# Hybrid Inheritance
# =====================================================

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound")


# class Mammal(Animal):
#     def give_birth(self):
#         print(f"{self.name} gives birth")


# class Bird(Animal):
#     def lay_eggs(self):
#         print(f"{self.name} lays eggs")


# class Flyable:
#     def fly(self):
#         print(f"{self.name} can fly")


# class FlyingBird(Bird, Flyable):
#     pass


# class NonFlyingBird(Bird):
#     def fly(self):
#         print(f"{self.name} cannot fly")


# class FlyingMammal(Mammal, Flyable):
#     pass

# class NonFlyingMammal(Mammal):
#     def fly(self):
#         print(f"{self.name} cannot fly")

# # Example usage
# sparrow = FlyingBird("Sparrow")
# penguin = NonFlyingBird("Penguin")
# cow = NonFlyingMammal("Cow")

# sparrow.fly()
# penguin.fly()
# cow.fly()
# =====================================================