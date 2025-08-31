# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Child class inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)   # call base class constructor
        self.storage = storage
        self.battery = battery
    
    # Encapsulation with getter and setter
    def get_battery(self):
        return self.battery
    
    def set_battery(self, new_battery):
        if 0 <= new_battery <= 100:
            self.battery = new_battery
        else:
            print("Battery percentage must be between 0 and 100.")
    
    def install_app(self, app_name):
        print(f"{app_name} has been installed on {self.device_info()}")

# Test the class
phone1 = Smartphone("Samsung", "Galaxy S22", "128GB", 85)
print(phone1.device_info())
phone1.install_app("WhatsApp")
print("Battery:", phone1.get_battery())
phone1.set_battery(95)  # update battery
print("Updated Battery:", phone1.get_battery())
