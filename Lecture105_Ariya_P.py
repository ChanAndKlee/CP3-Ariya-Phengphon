class Vehicle:
    licenseCar = ""
    serialCode = ""
    year = 0
    def turnOnAir(self):
        print("Turned on Air")
class Car(Vehicle):    # Class Car extends from Vehicle
    pass
class PickUp(Vehicle):
    VIPCard = False
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass

car1 = Car()
car1.turnOnAir()

pickUp1 = PickUp()
pickUp1.turnOnAir()

van1 = Van()
van1.turnOnAir()

estCar1 = EstateCar()
estCar1.turnOnAir()