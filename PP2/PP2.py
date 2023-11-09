# Ex 1
def getFibonacciElement(n):
   if n <= 1:
       return n
   else:
       return(getFibonacciElement(n-1) + getFibonacciElement(n-2))

def getFibonacciList(n):
    resultList = list()
    if n <= 0:
        print("Enter a positive number")
    else:
        for i in range(n):
            resultList.append(getFibonacciElement(i))        
    print(resultList)

print("***Exercitiul 1***")
nrFibonacciElements = 10
getFibonacciList(nrFibonacciElements)

# Ex 2
def isPrimeNumber(number):
    isPrime = True
    for i in range(2, (number // 2) + 1):
        if (number %i == 0):
            isPrime = False
    return isPrime

def getPrimeNumbersList(inputList):
    resultList = list()
    for number in inputList:
        if isPrimeNumber(number):
            resultList.append(number)     
    return resultList

print("***Exercitiul 2***")
primeNumbersCheckList = [2, 3, 4, 5, 11, 21, 23, 27, 31, 37, 38]
primeNumbers = getPrimeNumbersList(primeNumbersCheckList)
print(primeNumbers)

# Ex 3
def getListsIntersection(listA, listB):
    listIntersectionAB = [value for value in listA if value in listB]
    return listIntersectionAB

def getListsUnion(listA, listB):
    resultList = listA
    diffBMinusA = [i for i in listB if i not in listA]
    resultList.extend(diffBMinusA)
    return resultList

def getListsDifference(list1, list2):
    listDiff = [i for i in list1 if list2.count(i) == 0]
    return listDiff
 
print("***Exercitiul 3***")
listA = [5, 10, 15, 20, 25, 30, 35, 40, 45]
listB = [5, 9, 15, 21, 25, 31, 35, 41, 42]
print(getListsIntersection(listA, listB))
print(getListsUnion(listA, listB))
print(getListsDifference(listA, listB))
print(getListsDifference(listB, listA))

#Ex 5
def setZerosUnderMatrixDiagonal(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, i):
        # for j in range(len(matrix) - i, len(matrix)):
            matrix[i][j] = 0
    
print("***Exercitiul 5***")
matrixSize = 7
matrix = [[i + 1] * matrixSize for i in range(matrixSize)]   
setZerosUnderMatrixDiagonal(matrix)
for row in matrix:
    print(row)

#Ex 6 
def getListOfExactlyOccurances(nrOccurances, *lookoutLists):
    resultList = list()
    unionList = list()
    for list1 in lookoutLists:
        unionList += list1
    resultList = [element for element in unionList if unionList.count(element) == nrOccurances]
    return list(dict.fromkeys(resultList))

print("***Exercitiul 6***")
nrOfOccurances = 2
resultList = getListOfExactlyOccurances( nrOfOccurances, [1,2,3], [2,3,4], [4,5,6], [4,1, "test"])
print(resultList)

def isPalindrome(number):
    isPalindrome = False
    initialNumber = number
    reversedNumber = 0
    while number > 0:
        reversedNumber = reversedNumber * 10 + (number % 10)
        number = number // 10
    if reversedNumber == initialNumber:
        return True
    else:
        return False

#Ex 7
def palindromeCountAndMax(lookoutList):
    palindromeCount = 0
    maxPalindrome = -1
    palindromeList = [element for element in lookoutList if isPalindrome(element)]
    palindromeCount = len(palindromeList)
    maxPalindrome = max(palindromeList)
    return [palindromeCount, maxPalindrome]

print("***Exercitiul 7***")
palindromeLookoutList = [123, 11, 27, 121, 100, 17, 1]
palindromeInfo = tuple()
palindromeInfo = palindromeCountAndMax(palindromeLookoutList)
print(palindromeInfo)

#Ex 8
def getDivisibleByASCII(strList, flag, x=1):
    result = []
    for str in strList:
        list = []
        for character in str:
            if flag:
                if ord(character) % x == 0:
                    list += [character]
            else:
                if ord(character) % x != 0:
                    list += [character]
        result += [list]

    return result

print("***Exercitiul 8***")
divisibleByASCIILookoutList = ["test", "hello", "lab002"]
print(getDivisibleByASCII(divisibleByASCIILookoutList, False, 2))

#Ex 9
def getNoViewSpectators(matrix):
    resultList = [(i,j) for i in range(0, len(matrix)) for j in range(0, len(matrix[0])) for k in range(0, i) if matrix[k][j] >= matrix[i][j]]
    resultList = list(set(resultList))
    return resultList

print("***Exercitiul 9***")
matrix = [
    [1, 2, 3, 2, 1, 1], 
    [2, 4, 4, 3, 7, 2], 
    [5, 5, 2, 5, 6, 4], 
    [6, 6, 7, 6, 7, 5]
]
print(getNoViewSpectators(matrix))

#Ex 10
def getListsByPosition(*inputLists):
    maxLen = max([len(list) for list in inputLists])
    resultList = []
    for i in range(0, maxLen):
        positionList = []
        for list in inputLists:
            if len(list) <= i:
                positionList += [None]
            else:
                positionList += [list[i]]
        resultList += [positionList]
    return resultList

print("***Exercitiul 10***")
print(getListsByPosition([1, 2, 3, 4], [5, 6, 7], ["a", "b", "c"]))

#Ex 11
def orderTuplesCustom(tupleList):
    for i in range(0, len(tupleList) - 1):
        for j in range(i, len(tupleList)):
            if tupleList[i][1][2] > tupleList[j][1][2]:
                aux = tupleList[i]
                tupleList[i] = tupleList[j]
                tupleList[j] = aux

    return tupleList

print("***Exercitiul 11***")
print(orderTuplesCustom([('abc', 'bcd'), ('abc', 'zza')]))

#Ex 12
def getRhymesLists(wordList):
    result = list()
    rhymesList = [word[-2:] for word in wordList]
    rhymesList = list(dict.fromkeys(rhymesList))
    for rhyme in rhymesList:
        result += [[word for word in wordList if word[-2:] == rhyme]]
    return result

print("***Exercitiul 12***")
print(getRhymesLists(['ana', 'banana', 'carte', 'arme', 'parte']))