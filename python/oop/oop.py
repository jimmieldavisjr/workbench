
##########
#
# PYTHON OOP
# ----------------
#
# 1. Class-Based:
#       - Defines objects using classes with attributes and methods.
#
# 2. Uses 'self':
#       - Explicit reference to the instance in all instance methods.
#
# 3. Dynamic and Flexible:
#       - Attributes and methods can be added or modified at runtime.
#
# 4. No Access Modifiers:
#       - Public by default; underscores (_) indicate intended privacy.
#
# 5. Single and Multiple Inheritance:
#       - Supports both; method resolution order (MRO) manages conflicts.
#
# 6. Everything Is an Object:
#       - Classes, functions, modules, and types are all objects.
#
# 7. Encapsulation by Convention:
#       - Leading underscores signal protected/_private intent.
#
# 8. Supports Polymorphism:
#       - Duck typing: behavior is based on methods, not types.
#
# 9. Supports Abstraction:
#       - Via abstract base classes (ABC) and interfaces-style contracts.
#
##########

class Car:

    def __init__(self, make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"This {self.make} {self.model} is driving")

    def stop(self):
        print(f"This {self.make} {self.model} has stopped")

car_1 = Car("Lexus", "RX350", 2011, "Black")
car_2 = Car("Ford", "F150", 2020, "Silver")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_1.drive()
car_1.stop()
car_2.drive()
car_2.stop()