class Vehicle:
    def __init__(self, color, doors, tires, vtype):
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        #Stop the car
        return "%sBraking" % self.vtype
 
    def drive(self):
        #Drive the car
        return "I'm driving a %s %s!" % (self.color, self.vtype)

if __name__=="__main__":
    car = Vehicle("blue", 5, 4, "car")
    print(car.brake())
    print(car.drive())

    truck = Vehicle("red", 3, 6)
    print(truck.brake())
    print(truck.drive)