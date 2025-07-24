class Vehicle:
    """Base class for all vehicles"""
    
    def __init__(self, name, manufacturer,color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
    
    def drive(self):
        print("Driving", self.manufacturer,self.name)
    def turn(self, direction):
        print("Turning", self.name , "to", direction)
    def brake(self):
        print(self.name, "is Stopping!")
        
class Car(Vehicle):
    """Car class"""
    
    def __init__(self, name, manufacturer, color, year):
        super().__init__(name, manufacturer, color)
        self.year=2022
        self.wheels=4
        print("A new car has been created. Name:", self.name)
        print("It has:", self.wheels, "wheels")
        print("The car was built in,", self.year)
        
    def change_gear(self, gear_name):
        print( self.name , "is changing gear to", gear_name )
    
    def turn(self, direction):
       print( self.name , "is Turning" , direction)
    
if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupé", "Ford", "Red", 2022)
    v = Vehicle("Softtail Deluxe", "Harley-Davidson", "Blue")
    c.turn("Right")
    v.turn("Right")
    print(c.name, c.year, c.wheels)
    
class MotorCycle(Vehicle):
    """Motorcycle class"""
    
    def __init__(self, name, manufacturer, color, year):
        super().__init__(name, manufacturer, color)
        self.year=year
        self.wheels=4
        print("A new Motorcycle has been created. Name:", self.name)
        print("It has:", self.wheels, "wheels")
        print("The Motorcycle was built in,", self.year)
        
    def change_gear(self, gear_name):
        print( self.name , "is changing gear to", gear_name )
    
    def turn(self, direction):
       print( self.name , "is Turning" , direction)
    
if __name__ == "__main__":
    c = MotorCycle("NINJA H2®R", "Kawasaki", "Black", 2022)
    v = Vehicle("Softtail Deluxe", "Harley-Davidson", "Blue")
    c.turn("Right")
    v.turn("Right")
    print(c.name, c.year, c.wheels)
    print(v.name, v.manufacturer, v.color)