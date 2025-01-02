def ask_user_for_positive_integer() -> None:
    while True:
        user_input = input("Enter a positive integer (or done) ")
        if (user_input.lower() == "done"):
            return 0
        
        try:
            user_input_integer = int(user_input)  
        except ValueError as e:
            print("Not an integer- please try again")
            continue
                    
        if (user_input_integer > 0):
            return user_input_integer
        print("Input was incorrect")


def get_unique_integers(integer_list: list[int]) -> list[int]:
    """Given a list, return just the unique elements

    Args:
        integer_list (list[int]): list of input integers to be sorted into a unique list

    Returns:
        list[int]: a unique list of integers
    """
    # Sets only contain unique elements
    integer_set = set(integer_list)
    integer_list = list(integer_set)    
    return integer_list


def get_duplicate_integers(list_of_numbers: list[int]) -> list[int]:
    """Given a list of numbers, return a new list of numbers that contains any duplicate integers

    Args:
        list_of_numbers (list[int]): list containing numbers 

    Returns:
        list[int]: list of duplicate integers
    """
    integer_quantity = {}
    for integer in list_of_numbers:
        if (integer not in integer_quantity):
            integer_quantity[integer] = 1
            continue
        integer_quantity[integer] += 1
        
    duplicate_integers = []
    for integer in integer_quantity:
        if (integer_quantity[integer] != 1):
            duplicate_integers.append(integer)
            
    return duplicate_integers
       
        
def get_product_from_list(list_of_numbers: list[int]) -> int:
    """Calculates and returns the product of a list of numbers

    Args:
        list_of_numbers (list[int]): list containing numbers whose product is desired

    Returns:
        int: returns product of a list of numbers
    """
    product = 1
    for integer in list_of_numbers:
        product = product * integer
    return product


def get_range_from_list(list_of_numbers: list[int]) -> int:
    """Given a sorted list, with the smallest element at i=0 and largest element at i=len(list)-1, return the range"""
    # Given a sorted list, with the smallest element at i=0 and largest element at i=len(list)-1, return the range
    return list_of_numbers[len(list_of_numbers)-1] - list_of_numbers[0]


def get_sum_from_list(list_of_numbers: list[float]) -> float:
    """Calculates the sum of a /listOfNumbers/"""
    total_sum = 0
    for number in list_of_numbers:
        total_sum = total_sum + number
    return total_sum


def get_variance_from_list(list_of_numbers: list[int]) -> float:
    """Calculates the variance of the list of numbers provided"""
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


def seperate_odd_even_numbers(list_of_numbers: list[int]) -> list[list[int], list[int]]:
    """Seperates odd and even numbers into two lists, oddIntegers and evenIntegers"""
    odd_integers = []
    even_integers = []
    for num in list_of_numbers:
        if (num % 2 == 0):
            even_integers.append(num)
        else:
            odd_integers.append(num)

    odd_even_list = [odd_integers, even_integers]
    type(odd_even_list)
    return odd_even_list


def main():
    integer_list = []
    while True:
        userInteger = ask_user_for_positive_integer()
        if (userInteger == 0) or (len(integer_list) == 0):
            # User wants to see stats
            break
        integer_list.append(userInteger)
        
    unique_list = get_unique_integers(integer_list)
    duplicate_integers = get_duplicate_integers(integer_list)
    
    length = len(unique_list)
    product = get_product_from_list(integer_list)
    range = get_range_from_list(unique_list)
    variance = get_variance_from_list(unique_list)
    
    odd_numbers, even_numbers = seperate_odd_even_numbers(unique_list)

    print("Results:")
    duplicates = len(integer_list) - len(unique_list)
    print(f"{unique_list} (removed {duplicates} duplicates\n")
    if (len(even_numbers) == 0):
        print("No even numbers were provided.")
    if (len(odd_numbers) == 0):
        print("No odd numbers were provided.")

    print(f"{integer_list=} | {duplicate_integers=} | {unique_list=}")
    print(f"{variance=}, {length=}, {product=}, {range=}")
    print(f"{odd_numbers=}, {even_numbers=}")
    
    
main()