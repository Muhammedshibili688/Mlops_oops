# Initiate class
class Employee:
    # dunder/majic methods
    def __init__(self, name, id, designation):
        self.name = name
        self.id = id
        self.designation = designation

    def travel(self, destination = "London"):
        print("{0} travelling to destination {1}".format(self.name, destination))


# create object
Elon = Employee("Elon Musk", 1001, "CEO")

print(Elon.designation)
Elon.travel("New York")