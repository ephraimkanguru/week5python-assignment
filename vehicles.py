# Base class Vehicle
class Vehicle:
    def move(self):
        print("This vehicle is moving.")

# Subclass Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚲")

# Creating instances of each vehicle
my_car = Car()
my_plane = Plane()
my_bicycle = Bicycle()

# Calling the move() method on each vehicle
my_car.move()        # Output: Driving 🚗
my_plane.move()      # Output: Flying ✈️
my_bicycle.move()    # Output: Pedaling 🚲
