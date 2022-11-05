#create a Point class
class Point():
    def __init__(self,input1,input2):
        self.x=input1
        self.y=input2

p1=Point(1,2)
print(p1.x)
print(p1.y)

# creating a Flight class

class Flight():
    def __init__(self,maxCapacity):
        self.maxCapacity=maxCapacity
        self.passengers=[]
    #add passengers to the flight

    def addPassenger(self,name):
        # Pro ❤️‍🔥 way of doing this
        if not self.openSeat():
            return False
        self.passengers.append(name)
        return True

        # if len(self.passengers)<self.maxCapacity:
        #     self.passengers.append(name)
        # else:
        #     print("ERROR: Max capacity is full")
    def removePassenger(self,name):
        for passenger in self.passengers:
            print(passenger)
            if passenger==name:
                self.passengers.remove(name)
                print(f"{name} removed.")
                return
        
        print(f"ERROR: {name} is not in the flight")
    def refillFuel(self,liter):
        print("Filled fuel.")
    def openSeat(self):
        return self.maxCapacity-len(self.passengers)
flight=Flight(3)


people=["Manoj","Monu","Monika","Monuuu"]

for person in people:
    if flight.addPassenger(person):
        print(f"{person} is successfully added to the flight .")
    else:
        print(f"No available seat for {person}")


print(flight.passengers)

flight.removePassenger("Manoj")

flight.refillFuel(300)

print(flight.passengers)
