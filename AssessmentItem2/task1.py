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
    """Given a list, return just the unique elements

    Args:
        integerList (list[int]): list of input integers to be sorted into a unique list

    Returns:
        list[int]: a unique list of integers
    """
    # Sets only contain unique elements
    integerSet = set(integerList)
    integerList = list(integerSet)    
    return integerList


def GetDuplicateIntegers(listOfNumbers: list[int]) -> list[int]:
    """Given a list of numbers, return a new list of numbers that contains any duplicate integers

    Args:
        listOfNumbers (list[int]): list containing numbers 

    Returns:
        list[int]: list of duplicate integers
    """
    integerQuantity = {}
    for integer in listOfNumbers:
        if (integer not in integerQuantity):
            integerQuantity[integer] = 1
            continue
        integerQuantity[integer] += 1
        
    duplicateIntegers = []
    for integer in integerQuantity:
        if (integerQuantity[integer] != 1):
            duplicateIntegers.append(integer)
            
    return duplicateIntegers
       
        
def GetProductFromList(listOfNumbers: list[int]) -> int:
    """Calculates and returns the product of a list of numbers

    Args:
        listOfNumbers (list[int]): list containing numbers whose product is desired

    Returns:
        int: _description_
    """
    product = 1
    for integer in listOfNumbers:
        product = product * integer
    return product


def GetRangeFromList(listOfNumbers: list[int]) -> int:
    """Given a sorted list, with the smallest element at i=0 and largest element at i=len(list)-1, return the range

    Args:
        listOfNumbers (list[int]): sorted list containing numbers (smallest number at index 0) whose range is desired

    Returns:
        int: range of the list. largest element - smallest element
    """
    # Given a sorted list, with the smallest element at i=0 and largest element at i=len(list)-1, return the range
    return listOfNumbers[len(listOfNumbers)-1] - listOfNumbers[0]


def GetSumFromList(listOfNumbers: list[float]) -> float:
    """Calculates the sum of a /listOfNumbers/

    Args:
        listOfNumbers (list[float]): list containing numbers whose sum is desired

    Returns:
        float: sum of the list
    """
    sum = 0
    for number in listOfNumbers:
        sum = sum + number
    return sum


def GetVarianceFromList(listOfNumbers: list[int]) -> float:
    """Calculates the variance of the list of numbers provided

    Args:
        listOfNumbers (list[int]): list containing numbers whose variance is desired

    Returns:
        float: variance of the list
    """
    listLength = len(listOfNumbers)
    if listLength == 0:
        return listLength
    
    sum = GetSumFromList(listOfNumbers)
    mean = sum / listLength
    
    squaredDifferences = []
    for number in listOfNumbers:
        squaredDifference = (number - mean) ** 2
        squaredDifferences.append(squaredDifference)
        
    variance = GetSumFromList(squaredDifferences) / listLength
    return variance


def SeperateOddEvenNumbers(listOfNumbers: list[int]) -> list[list[int], list[int]]:
    """Seperates odd and even numbers into two lists, oddIntegers and evenIntegers

    Args:
        listOfNumbers (list[int]): presorted list of integers

    Returns:
        list[list[int], list[int]]: returns a list of two lists: [oddIntegers, evenIntegers]
    """
    oddIntegers = []
    evenIntegers = []
    for num in listOfNumbers:
        if (num % 2 == 0):
            evenIntegers.append(num)
        else:
            oddIntegers.append(num)

    seperateLists = [oddIntegers, evenIntegers]
    return seperateLists


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