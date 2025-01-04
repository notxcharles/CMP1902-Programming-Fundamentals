# task1.py - Charles Frederick Harrison 25320877
def ask_user_for_positive_integer() -> int | None:
    while True:
        user_input = input("Enter a positive integer (or done) ")
        print(f"{user_input=}")
        if (user_input.lower() == "done"):
            return 0
        if not user_input.isdigit():
            print("Only positive integers are allowed!", "Numbers with decimals, negative numbers or characters will not be accepted")
            continue
        if (int(user_input) > 0):
            return int(user_input)
        print("Input was incorrect")
    return


def get_unique_integers(integer_list: list[int]) -> list[int]:
    """Given a list, return a list of the unique elements"""
    # Sets only contain unique elements
    integer_set = set(integer_list)
    integer_list = list(integer_set)    
    return integer_list


def get_duplicate_integers(list_of_numbers: list[int]) -> list[int]:
    """Given a list of numbers, return a new list of numbers that contains any duplicate integers"""
    integer_quantity = dict()
    for integer in list_of_numbers:
        if (integer not in integer_quantity):
            integer_quantity[integer] = 1
            continue
        integer_quantity[integer] += 1
        
    duplicate_integers = []
    for integer in integer_quantity:
        if (integer_quantity[integer] > 1):
            duplicate_integers.append(integer)
            
    return duplicate_integers
       
        
def get_product_from_list(list_of_numbers: list[int]) -> int:
    """Calculates and returns the product of a list of numbers"""
    product = 1
    for number in list_of_numbers:
        product = product * number
    return product


def get_range_from_list(list_of_numbers: list[int]) -> int:
    """Given a list, return the range, list[-1] - list[0]"""
    sorted_set = set(list_of_numbers)
    sorted_list = list(sorted_set)
    return sorted_list[-1] - sorted_list[0]


def get_sum_from_list(list_of_numbers: list[float]) -> float:
    """Calculates the sum of a /listOfNumbers/"""
    total_sum = 0
    for number in list_of_numbers:
        total_sum = total_sum + number
    return total_sum


def get_variance_from_list(list_of_numbers: list[int]) -> float:
    """Calculates the variance of the /list_of_numbers/"""
    list_length = len(list_of_numbers)
    if list_length == 0:
        return list_length
    
    total_sum = get_sum_from_list(list_of_numbers)
    mean = total_sum / list_length
    
    squared_differences = []
    for number in list_of_numbers:
        squared_difference = (number - mean) ** 2
        squared_differences.append(squared_difference)

    variance = get_sum_from_list(squared_differences) / list_length
    return variance


def separate_odd_even_numbers(list_of_numbers: list[int]) -> [list[int], list[int]]:
    """Separates odd and even numbers into two lists of odd Integers and even Integers"""
    odd_integers = []
    even_integers = []
    for num in list_of_numbers:
        if (num % 2 == 0):
            even_integers.append(num)
        else:
            odd_integers.append(num)
    return odd_integers, even_integers


def main():
    integer_list = []
    while True:
        # Prompts the user to input only positive integer numbers
        # User can input 'done' to view statistics (provided that they have input a number)
        user_integer = ask_user_for_positive_integer()
        if (user_integer == 0):
            # User hasn't entered a valid number, we can't see the stats yet
            if (len(integer_list) == 0):
                continue
            break
        integer_list.append(user_integer)

    # Get unique and duplicate numbers
    unique_list = get_unique_integers(integer_list)
    duplicate_integers = get_duplicate_integers(integer_list)

    print("\nResults:")
    duplicates = len(integer_list) - len(unique_list)
    print(f"Removed {duplicates} duplicates!")
    if (duplicates != 0):
        print(f"Duplicate numbers: {duplicate_integers}")
    print(f"Your unique list of numbers: {unique_list}")

    length = len(unique_list)
    print(f"There are {length} of unique integers in the list!")

    product = get_product_from_list(integer_list)
    print(f"The product of the list is {product}!")
    list_range = get_range_from_list(unique_list)
    print(f"The range of the list is {list_range}!")
    variance = get_variance_from_list(unique_list)
    print(f"The variance of the list is {variance:.2f}!")
    
    odd_numbers, even_numbers = separate_odd_even_numbers(unique_list)
    if (len(even_numbers) == 0):
        print("No even numbers were provided!")
    if (len(odd_numbers) == 0):
        print("No even numbers were provided!")
    
    
main()