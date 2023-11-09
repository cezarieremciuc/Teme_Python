from Shape import Circle, Rectangle, Triangle
from BankAccount import SavingsAccount, CheckingAccount
from Vehicle import Car, Motorcycle, Truck
from Employee import Manager, Engineer, Salesperson
from Animal import Mammal, Bird, Fish

if __name__ == "__main__":
# Ex1
    # Circle
    circle1 = Circle(2)
    print("\nCircle:")
    print(f"Area: {circle1.getArea()}")
    print(f"Perimeter: {circle1.getPerimeter()}")

    # Rectangle
    rectangle1 = Rectangle(2,3)
    print("\nRectangle:")
    print(f"Area: {rectangle1.getArea()}")
    print(f"Perimeter: {rectangle1.getPerimeter()}")

    # Triangle
    triangle1 = Triangle(2,3,4)
    print("\nTriangle:")
    print(f"Area: {triangle1.getArea()}")
    print(f"Perimeter: {triangle1.getPerimeter()}")

# Ex2
    # SavingsAcoount
    savingsAccount1 = SavingsAccount()
    print("\nSavings account:")

    savingsAccount1.deposit(2000)
    print(savingsAccount1.balance)

    savingsAccount1.withdrawal(200)
    print(savingsAccount1.balance)

    print(savingsAccount1.getInterestValue(5))

    # CheckingAccount
    checkingAccount1 = CheckingAccount()
    print("\Checking account:")

    checkingAccount1.deposit(2000)
    print(checkingAccount1.balance)

    checkingAccount1.withdrawal(200)
    print(checkingAccount1.balance)

    print(checkingAccount1.getInterestValue(10))

# Ex3
    car = Car("Toyota", "Camry", 2022, 1850, 2000)
    print("\nCar:")
    print(car.calcMileage())
    print(car.calcTowingCapacity())
    
    # Creating a motorcycle instance
    motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021, 180, 200)
    print("\nMotorcycle:")
    print(motorcycle.calcMileage())
    print(motorcycle.calcTowingCapacity())
    
    # Creating a truck instance
    truck = Truck("Ford", "F-150", 2020, 15000, 12000, 1190)
    print("\nTruck:")
    print(truck.calcMileage())
    print(truck.calcTowingCapacity())

# Ex4
    manager = Manager("Gervonta Davis", 10)
    print("\nManager:")
    # print(manager)
    manager.applyRaise(5000)
    print(manager)
    
    # Creating a motorcycle instance
    engineer = Engineer("Tyson Fury", 12)
    print("\nEngineer:")
    # print(engineer)
    engineer.addExtraHours(10)
    print(engineer)
    engineer.addSubordinates(Manager("Dillian White", 5))
    engineer.addSubordinates(Manager("Anthony Joshua", 6))
    engineer.addSubordinateExtraHours("Anthony Joshua", 30)
    print(engineer)
    
    # Creating a truck instance
    salesperson = Salesperson("Ariany Celeste", 6, 0.1)
    print("\nSalesperson:")
    # print(salesperson)
    salesperson.addCommision(2000)
    # print(salesperson)
    salesperson.makeSale(2000)
    salesperson.makeSale(5000)
    salesperson.makeSale(1000)
    print(salesperson)

    # Mammal
    mammal = Mammal("Cheetah", True, False, False, False, 70)
    print("\nMammal:")
    print(mammal)
    print(mammal.getMaturity())

    # Bird
    bird = Bird("Eagle", True, False, False, False, 2.5)
    print("\nBird:")
    print(bird)
    print(bird.wingLength())

    # Fish
    fish = Fish("Tuna", True, False, True, False, 200)
    print("\nFish:")
    print(fish.getTypeByDepth())
    print(fish)