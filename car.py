class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make.title()} {self.model.title()}"
        return long_name

    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it")

    def update_odometer(self, mileage):
        self.odometer = mileage

    def increment_odometer(self, miles):
        self.odometer += miles


my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(2000)
my_used_car.read_odometer()

my_used_car.increment_odometer(5)
my_used_car.read_odometer()
