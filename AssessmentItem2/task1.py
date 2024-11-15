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
    
    
main()