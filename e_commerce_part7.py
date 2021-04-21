class Car:
    def __init__(self,name,engine,torque):
        self.name = name
        self.engine = engine
        self.torque = torque

    def accelerate(self):
        print(self.name+" is accelerating.")
        return self.torque

    @classmethod
    def works(self):
        print("Works...")

# engine = int(input("Enter value of engine: "))
swift = Car("Swift",1197,115)
fortuner = Car("Fortuner",2500,500)
x = swift.accelerate()
print(x)
fortuner.accelerate()
Car.works()
print(swift.engine,swift.torque)
print(fortuner.engine,fortuner.torque)