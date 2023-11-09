import datetime

class Vehicle:
    avgMileagePerYear = 0
    gvwr = 0 # GVWR = gross vehicle weight rating
    curbWeight = 0

    def __init__(self, make, model, year):      
        self.make = make
        self.model = model
        self.year = year

    def calcMileage(self):
        today = datetime.date.today()
        year = today.year
        return (year - self.year) * self.avgMileagePerYear

    # GVWR – curb weight – truck body additions = payload capacity with truck add-ons
    # 9,000 kg – 6,000 kg – 1,190 kg = 1,810 kg payload capacity
    def calcTowingCapacity(self):
        return self.gvwr + self.curbWeight
 
 
class Car(Vehicle):
    def __init__(self, make, model, year, curbWeight, gvwr):
        super().__init__(make, model, year)
        self.curbWeight = curbWeight
        self.gvwr = gvwr
        self.avgMileagePerYear = 20000

 
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, curbWeight, gvwr):
        super().__init__(make, model, year)
        self.curbWeight = curbWeight
        self.gvwr = gvwr
        self.avgMileagePerYear = 10000
 
 
class Truck(Vehicle):
    def __init__(self, make, model, year, curbWeight, gvwr, tba):
        super().__init__(make, model, year)
        self.curbWeight = curbWeight
        self.gvwr = gvwr
        self.tba = tba # truck body additions
        self.avgMileagePerYear = 100000

    def calcTowingCapacity(self):
        return self.gvwr + self.curbWeight + self.tba
 
