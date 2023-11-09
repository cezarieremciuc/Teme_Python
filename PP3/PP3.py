#Ex 1
def getOperationsResult(list1, list2):
    resultList = list()
    resultList += [ set(list1) & set(list2) ]
    resultList += [ set(list1) | set(list2) ]
    resultList += [ set(list1) - set(list2) ]
    resultList += [ set(list2) - set(list1) ]
    return resultList
    
print("***Exercitiul 1***")
print(getOperationsResult([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))

#Ex 2
def getCustomDictFromString(inputStr):
    dictStr = {i:inputStr.count(i) for i in inputStr}
    return dictStr

print("***Exercitiul 2***")
print(getCustomDictFromString("Ana has apples."))

#Ex 4
def buildXmlElement(tag, content, **properties):
    resultStr = ""
    propertyStrConcat = ""
    firstTagStr = "<" + tag + ">"
    resultStr += firstTagStr
    resultStr += content + "</" + tag + ">"
    propertyStr = [str(item[0]) + "=" + "\\" + "\"" + str(item[1]) + "\\" + "\"" for item in properties.items()]
    propertyAreaStartIndex = resultStr.index(firstTagStr) + len(firstTagStr) - 1
    for i in propertyStr:
        propertyStrConcat += i
    resultStr = resultStr[ : propertyAreaStartIndex] + " " + propertyStrConcat + resultStr[propertyAreaStartIndex : ]
    return resultStr

print("***Exercitiul 4***")
print(buildXmlElement("a", "Hello there", href = " http://python.org ", _class = " my-link ", id = " someid "))

#Ex 5
def validateDict(ruleSet, inputDict):
    appliedRule = tuple()
    rulesKeyList = [i[0] for i in ruleSet]
    for key in inputDict:
        if rulesKeyList.count(key) == 0:
            return False
        else:
            appliedRule = [i for i in ruleSet if i[0] == key][0]
            dictValueStr = str(inputDict[key])
            if dictValueStr.startswith(appliedRule[1]) == False or dictValueStr.endswith(appliedRule[3]) == False or dictValueStr.find(appliedRule[2], 1, -1) == -1:
                return False
    return True

validationRules = {("key1", "", "inside", ""), ("key2", "prefix", "middle", "suffix")}#, ("key3", "this", "not", "valid")
dictionaryToValidate = {"key1": "come inside, it's too cold out", "key2": "prefix come inside middle, it's too cold out suffix", "key3": "this is not valid"}
print("***Exercitiul 5***")
print(validateDict(validationRules, dictionaryToValidate))

#Ex 6
def getUniqueAndDuplicatedInfo(inputList):
    inputSet = set(inputList)
    dublicatedSet = set(filter(lambda e : inputList.count(e) > 1, inputList))
    return (len(inputSet), len(dublicatedSet))

print("***Exercitiul 6***")
inputList6 = [1, 2, 3, 1, 5, 3, 3]
print(getUniqueAndDuplicatedInfo(inputList6))

#Ex 7
def getSetsOperations(*inputSets):
    inputSetsList = list(inputSets)
    resultDict = dict()
    for i in range(0, len(inputSetsList) - 1):
        for j in range(i + 1, len(inputSetsList)):
            resultDict.update({str(inputSetsList[i]) + " | " + str(inputSetsList[j]) : inputSetsList[i] | inputSetsList[j]})
            resultDict.update({str(inputSetsList[i]) + " & " + str(inputSetsList[j]) : inputSetsList[i] & inputSetsList[j]})
            resultDict.update({str(inputSetsList[i]) + " - " + str(inputSetsList[j]) : inputSetsList[i] - inputSetsList[j]})
            resultDict.update({str(inputSetsList[j]) + " & " + str(inputSetsList[i]) : inputSetsList[j] - inputSetsList[i]})
    return resultDict

print("***Exercitiul 7***")
print(getSetsOperations({1, 2, 4}, {2, 3, 5}, {7, 8, 1}))

#Ex 8
def customLoopDict(inputDict):
    resultList = list()
    endLoop = False
    resultList.append(inputDict["start"])
    while not endLoop:
        nextKey = resultList[-1]
        if inputDict[nextKey] in resultList:
            endLoop = True
        else:
            resultList.append(inputDict[nextKey])
    return resultList

print("***Exercitiul 8***")
print(customLoopDict({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

#Ex 9
def getPositionalArgsFound(*posArgs, **keywordArgs):
    posArgsSet = set(posArgs)
    keywordArgsSet = set(keywordArgs.values())
    return len(posArgsSet & keywordArgsSet)

print("***Exercitiul 9***")
print(getPositionalArgsFound(1, 2, 3, 4, x=1, y=2, z=3, w=5))