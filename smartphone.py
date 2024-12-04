#  Smartphone class
class Smartphone:
    # Constructor to initialize the smartphone's attributes
    def __init__(self, brand, model, battery_percentage, price):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage
        self.price = price

    # Method to simulate making a call
    def make_call(self):
        print(f"{self.model} is making a call...")

    # Method to simulate taking a picture
    def take_picture(self):
        print(f"{self.model} is taking a picture...")

    # Method to simulate charging the battery
    def charge_battery(self):
        self.battery_percentage = 100
        print(f"{self.model} is charging. Battery is now {self.battery_percentage}%.")
        
# Creating an instance of the Smartphone class
my_phone = Smartphone("Samsung", "Galaxy S21", 80, 800)

# Calling methods on the instance
my_phone.make_call()  # Calls the make_call method
my_phone.charge_battery()  # Calls the charge_battery method


# New SmartphoneWithCamera class (inherits from Smartphone)
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_percentage, price, camera_quality):
        # Call the parent class constructor (Smartphone)
        super().__init__(brand, model, battery_percentage, price)
        self.camera_quality = camera_quality  # New attribute for camera quality

    # Method to take a high-quality picture
    def take_high_quality_picture(self):
        print(f"{self.model} is taking a high-quality picture with {self.camera_quality} MP camera!")

# Creating an instance of the SmartphoneWithCamera class
my_camera_phone = SmartphoneWithCamera("Samsung", "Galaxy S21 Ultra", 85, 1200, 108)

# Calling methods from both the parent (Smartphone) and child (SmartphoneWithCamera) classes
my_camera_phone.make_call()  # From Smartphone class
my_camera_phone.take_picture()  # From Smartphone class
my_camera_phone.take_high_quality_picture()  # From SmartphoneWithCamera class
