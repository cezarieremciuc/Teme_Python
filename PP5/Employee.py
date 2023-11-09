class Employee:
    monthlyWorkingHours = 40 * 4
    minPayHour = 3
      
    def __init__(self, name, hourlyPay):
        self.name = name
        self.extraWorkHours = 0
        self.extraHourlyPay = 2 * hourlyPay
        self.commision = 0
        if hourlyPay >= Employee.minPayHour:
            self.hourlyPay = hourlyPay
        else:
            self.hourlyPay = Employee.minPayHour

    def applyRaise(self, value):
        self.hourlyPay += int(value / self.monthlyWorkingHours)

    def calculatePayroll(self):
        return self.monthlyWorkingHours * self.hourlyPay + self.extraWorkHours * self.extraHourlyPay + self.commision
    
    def addExtraHours(self, hours):
        self.extraWorkHours += hours

    def addCommision(self, value):
        self.commision += value

    def __str__(self):
        return (f"Employee {self.name}, worked {self.monthlyWorkingHours}+{self.extraWorkHours} h, salary: {self.calculatePayroll()}")
    
    def addSubordinates():
        pass

class Manager(Employee):
    def __init__(self, name, hourlyPay):
        super().__init__(name, hourlyPay)
        self.subordinateEmp = []
    
    def addSubordinates(self, employee):
        self.subordinateEmp.append(employee)
    
    def giveRaise(self, employeeName, raiseValue):
        for employee in self.subordinateEmp:
            if employee.name == employeeName:
                employee.applyRaise(raiseValue)
 
class Engineer(Employee):
    def __init__(self, name, hourlyPay):
        super().__init__(name, hourlyPay)
        self.subordinateEmp = []

    def addSubordinates(self, employee):
        self.subordinateEmp.append(employee)
        
    def addSubordinateExtraHours(self, employeeName, hours):
        for employee in self.subordinateEmp:
            if employee.name == employeeName:
                employee.addExtraHours(hours)
 
class Salesperson(Employee):
    def __init__(self, name, hourlyPay, saleCommisionRate):
        super().__init__(name, hourlyPay)
        self.saleCommisionRate = saleCommisionRate
        self.totalSales = 0

    def makeSale(self, value):
        self.totalSales += value

    def calculatePayroll(self):
        return self.monthlyWorkingHours * self.hourlyPay + self.extraWorkHours * self.extraHourlyPay + (self.saleCommisionRate * self.totalSales / 100 )
