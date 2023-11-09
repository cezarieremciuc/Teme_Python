class Animal:
    def __init__(self, name, isCarnivore, isHerbivore, isSociable = True, isDomestic = False):
        self.name = name
        self.isCarnivore = isCarnivore
        self.isHerbivore = isHerbivore
        self.isSociable = isSociable
        self.isDomestic = isDomestic

    def isOmnivore(self):
        return self.isCarnivore and self.isHerbivore 
    
    def isSolitary(self):
        return not self.isSociable

    def __str__(self):
        pass
 
 
class Bird(Animal):
    def __init__(self, name, wingspan, isCarnivore, isHerbivore, isSociable, isDomestic):
        super().__init__(name, isCarnivore, isHerbivore, isSociable, isDomestic)
        self.wingspan = wingspan
 
    def wingLength(self):
        return self.wingspan
    
    def __str__(self):
        return (f"Animal {self.name}, wingspan {self.wingspan}m, diet: {self.isOmnivore()}, social: {self.isSociable}, pet: {self.isDomestic}")
 
 
class Fish(Animal):
    def __init__(self, name, maxDepth, isCarnivore, isHerbivore, isSociable, isDomestic):
        super().__init__(name, isCarnivore, isHerbivore, isSociable, isDomestic)
        self.maxDepth = maxDepth
 
    def getTypeByDepth(self):
        if self.maxDepth < 10:
            return "Shallow fish"
        elif self.maxDepth > 100:
            return "Deep fish"
        else:
            return "Medium fish"
        
    def __str__(self):
        return (f"Animal {self.name}, swims up to {self.maxDepth}m, diet: {self.isOmnivore()}, social: {self.isSociable}, pet: {self.isDomestic}")
 
 
class Mammal(Animal):
    def __init__(self, name, weight, isCarnivore, isHerbivore, isSociable, isDomestic):
        super().__init__(name, isCarnivore, isHerbivore, isSociable, isDomestic)
        self.weight = weight
 
    def getMaturity(self):
        if self.weight < 1:
            return "Cub"
        elif self.weight > 200:
            return "Giant"
        else:
            return "Normal"
        
    def __str__(self):
        return (f"Animal {self.name}, weight {self.weight}kg, diet: {self.isOmnivore()}, social: {self.isSociable}, pet: {self.isDomestic}")
 
 