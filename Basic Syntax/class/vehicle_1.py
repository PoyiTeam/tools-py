class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def showProperty(self):
        print("Vehicle name:", self.name)
        print("Vehicle color:", self.color)
        print("Vehicle weight:", self.weight)
    
    def accelerator(self, boost):
        acceleration = boost * self.acceleration_rate
        duration = round(100 / acceleration, 1)
        print("It takes", duration,"seconds for my", self.name, "to accelerate from 0 to 100km/hr.")
    
class car(Vehicle):
    weight = 1.2
    color = "blue"
    acceleration_rate = 10

class bus(Vehicle):
    weight = 10
    color = "green"
    acceleration_rate = 5

myCar = car("toyota")
myCar.accelerator(boost=0.6)
myBus = bus("統聯")
myBus.accelerator(boost=0.6)

# dir(myCar)