def AskUserForPositiveInteger() -> None:
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


def GetDuplicateIntegers(originalElements: list[int]) -> list[str]:
    integerQuantity = {}
    for integer in originalElements:
        if (integer not in integerQuantity):
            integerQuantity[integer] = 1
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


def SeperateOddEvenNumbers(listOfNumbers: list[int]) -> list[list[int], list[int]]:
    oddIntegers = []
    evenIntegers = []
    for num in listOfNumbers:
        if (num % 2 == 0):
            evenIntegers.append(num)
        else:
            oddIntegers.append(num)
            
    return [oddIntegers, evenIntegers]


def main():
    integerList = []
    while True:
        userInteger = AskUserForPositiveInteger()
        if userInteger == 0:
            # User wants to see stats
            break
        integerList.append(userInteger)
        
    uniqueList = GetUniqueIntegers(integerList)
    duplicateIntegers = GetDuplicateIntegers(integerList)
    
    length = len(uniqueList)
    product = GetProductFromList(integerList)
    range = GetRangeFromList(uniqueList)
    variance = GetVarianceFromList(uniqueList)
    
    oddNumbers, evenNumbers = SeperateOddEvenNumbers(uniqueList)
    if (len(evenNumbers) == 0):
        print("No even numbers were provided.")
    if (len(oddNumbers) == 0):
        print("No odd numbers were provided.")

    print(f"{integerList=} | {duplicateIntegers=} | {uniqueList=}")
    print(f"{variance=}, {length=}, {product=}, {range=}")
    print(f"{oddNumbers=}, {evenNumbers=}")
    
    
main()