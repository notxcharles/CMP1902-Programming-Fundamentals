def AskUserForPositiveInteger():
    while True:
        userInput = input("Enter a positive integer (or done) ")
        if (userInput.lower() == "done"):
            return 0
        
        try:
            userInputInteger = int(userInput)  
        except ValueError as e:
            print("Not an integer- please try again")
            continue
                    
        if (userInputInteger > 0):
            return userInputInteger
        
        print("Input was incorrect")


def GetUniqueIntegers(integerList: list[int]) -> list[int]:
    # Sets only contain unique elements
    integerSet = set(integerList)
    integerList = list(integerSet)    
    return integerList


def GetDuplicateIntegers(originalElements: list[int], uniqueElements: list[str]) -> list[str]:
    integerQuantity = {}
    for integer in originalElements:
        if (integer not in integerQuantity):
            integerQuantity[integer] = 0
            continue
        integerQuantity[integer] += 1
        
    duplicateIntegers = []
    for integer in integerQuantity:
        if (integerQuantity[integer] != 1):
            duplicateIntegers.append(integer)
            
    return duplicateIntegers
        
def GetProductFromList(targetList: list[str]) -> int:
    product = 1
    for integer in targetList:
        product = product * integer
    return product

def GetRangeFromList(targetList: list[str]) -> int:
    # Given a sorted list, with the smallest element at i=0 and largest element at i=len(list)-1, return the range
    return targetList[len(targetList)-1] - targetList[0]

def GetSumFromList(listOfNumbers: list[float]) -> float:
    sum = 0
    for number in listOfNumbers:
        sum = sum + number
    return sum

def GetVarianceFromList(listOfNumbers: list[int]) -> float:
    listLength = len(listOfNumbers)
    if listLength == 0:
        return listLength
    
    sum = GetSumFromList(listOfNumbers)
    mean = sum / listLength
    
    squaredDifferences = []
    for number in listOfNumbers:
        squaredDifference = (number - mean) ** 2
        squaredDifferences.append(squaredDifference)
        
    variance = GetSumFromList(squaredDifferences) 
    vardiv = variance / listLength
    return vardiv

def main():
    integerList = []
    while True:
        userInteger = AskUserForPositiveInteger()
        if userInteger == 0:
            # user wants to see stats
            break
        integerList.append(userInteger)
        
    uniqueList = GetUniqueIntegers(integerList)
    duplicateIntegers = GetDuplicateIntegers(integerList, uniqueList)
    print(f"{duplicateIntegers=} | {integerList=} | {uniqueList=}")
    
    length = len(uniqueList)
    product = GetProductFromList(integerList)
    range = GetRangeFromList(uniqueList)
    variance = GetVarianceFromList(uniqueList)
    print(f"{variance=}, {length=}, {product=}, {range=}")
    
    
    
main()