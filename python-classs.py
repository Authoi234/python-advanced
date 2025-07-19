class Car:
    def __init__(self, name, manufacturer, year, engine_cc, color):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year
        self.engine_cc = engine_cc
        self.color = color
    def start(self):
        print(f"Starting the engine with power {self.engine_cc}...")
    def brake(self):
        print(f"Braking the engine with power {self.engine_cc}...")
        print("Car Braked")
    def drive(self):
        print(f"Driving the {self.name} with engine power of {self.engine_cc}...")
    def turn(self, direction):
        print(f"Turning The Car {direction} with  engine power {self.engine_cc}...")
    def changeGear(self, gear):
        print(f"Changing the gear to {gear} with  engine power {self.engine_cc}...")

my_Lamborghini = Car("Lamborghini Aventador", "Lamborghini", 2023, 5000, "Red")
my_Lamborghini.start()
my_Lamborghini.drive()
my_Lamborghini.turn("left")
my_Lamborghini.changeGear("D")
my_Lamborghini.brake()
print(my_Lamborghini.name, my_Lamborghini.manufacturer, my_Lamborghini.year, my_Lamborghini.engine_cc, my_Lamborghini.color)
print("Lamborghini object created successfully.")
my_bugatti = Car("Bugatti Chiron", "Bugatti", 2023, 8000, "Blue")
print(my_bugatti.name, my_bugatti.manufacturer, my_bugatti.year, my_bugatti.engine_cc, my_bugatti.color)
my_bugatti.start()
my_bugatti.drive()
my_bugatti.turn("right")
my_bugatti.changeGear("C")
my_bugatti.brake()
print("Bugatti object created successfully.")
    