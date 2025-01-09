
# NO IMPORTS :)

def clear_screen():
    """Function to clear the screen (only works on some terminals)"""
    print("\033c", end="") # Clear the screen


def get_positive_numbers() -> list:
    """Function to ask the user to enter a specified amount of integers.

    Returns:
        list: The list of entered numbers from the user.
    """
    
    clear_screen()
    
    positive_ints = list()

    while True:
        clear_screen()
        print("\n\nPlease enter the amount of numbers you'd like to enter below.")
        try:
            input_amount: int = int(input(" :: ").strip())
            break
        except:
            print("Please enter a valid integer.")
        
    # Loops the amount of times the user had input
    for i in range(0, input_amount):
        # Loops until a correct input is present which breaks the loop
        while True:  
            
            clear_screen()
            print(f"\nYour entered numbers so far\n\t:: {positive_ints}")
            print(f"\nNumbers remaining: {input_amount - i}")
            print("\nPlease enter a positive whole number.")
            
            # If there is an input and its a positive integer, add it to the listenter a positive number.
            try:
                num_input: int = int(input(" :: ").strip())
                positive_ints.append(num_input)
                break
            except:
                print("Please enter a valid integer.")

    return positive_ints


def remove_duplicates(numbers: list) -> list:
    """Takes the users entered numbers as a parameter and removes any duplicate numbers
    from the list.

    Args:
        numbers (list, optional): The user's entered numbers.

    Returns:
        list: The list of only unique numbers.
    """
    unique_nums: list = list()
    duplicate_nums: list = list()

    # Seperates duplicates and unique numbers.
    for i in range(len(numbers)):
        if numbers[i] not in unique_nums:
            unique_nums.append(numbers[i])
        else:
            duplicate_nums.append(numbers[i]) 

    return unique_nums, duplicate_nums


def calculate_product(numbers: list) -> int:
    """Simple function to calculate the product of the numbers

    Args:
        numbers (list, optional): _description_.

    Returns:
        int: _description_
    """
    # Loops through all numbers multiplying them together.
    running_total: int = 1
    for i in numbers:
        running_total *= i

    return running_total


def calculate_range(numbers: list) -> int:
    """Function to calculate the range of a given list of numbers.

    Args:
        numbers (list): The list of numbers.

    Returns:
        int: The range of the numbers.
    """
    nums_range: int = 0

    # Find the larges and smallest values
    largest: int = 0
    smallest: int = 100000000000000
    for i in numbers:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
    
    # Find the difference in those values
    nums_range = largest - smallest
    
    return nums_range


def calculate_variance(numbers: list) -> int:
    """Function to calculate the variance of a given list of numbers.

    Args:
        numbers (list): The list of numbers.


    Returns:
        int: The variance of the numbers.
    """
    nums_var: int = 0

    # Calculate the mean of the data
    data_mean: int = 0
    numbers_sum: int = 0
    for i in numbers:
        numbers_sum += i
    data_mean = numbers_sum / len(numbers)

    # Find each data point's difference from the mean
    # Sqaure each of these values
    # Add up all these values
    mean_diff: int = 0
    for j in numbers:
        mean_diff += (j - data_mean)**2 

    # Divide this by the N of the population
    nums_var = mean_diff / len(numbers)
    return nums_var


def separate_even_odd(numbers: list) -> list:
    """Function to seperate the odd and even numbers into two lists

    Args:
        numbers (list): The list of numbers. 

    Returns:
        list, list: The even, and odd list repsectively
    """
    even_numbers = []
    odd_numbers = []

    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)
        elif i % 2 != 0:
            odd_numbers.append(i)
        else:
            print("Error calculating odd and even numbers.")
    

    return even_numbers, odd_numbers

def display_results(
    numbers, unique_numbers, duplicate_numbers, even_numbers, 
    odd_numbers, count, product, range_val, variance
    ):
    """Function to control all the values being displayed

    Args:
        unique_numbers (_type_): The amount of unique numbers.
        removed_duplicates (_type_): The list of unique numbers.
        even_numbers (_type_): The list of even numbers.
        odd_numbers (_type_): The list of odd numbers.
        count (_type_): The amount of numbers.
        product (_type_): The product of the numbers.
        range_val (_type_): The range of the numbers.
        variance (_type_): The variance of the numbers.
    """
    
    clear_screen()
    
    # Outputs
    print(f"""
Your results:

You entered:
\t:: {numbers}

A total of {count} numbers.
""")

    # Unique Numbers
    print(
        "\nYour set contained no unqiue numbers." 
        if len(unique_numbers) == 0
        else f"\nYour set of unique numbers:\n\t::{unique_numbers}"
        )
    
    # Duplicate Numbers
    print(
        "\nYour set contained no duplicate numbers." 
        if len(duplicate_numbers) == 0
        else f"\nYour set of duplcaite numbers:\n\t::{duplicate_numbers}"
        )
    
    # Even Numbers
    print(
        "\nYour set contained no even numbers."
        if len(even_numbers) == 0
        else f"\nEven :: {len(even_numbers)} numbers\n\t::{even_numbers}"
        )  
    
    # Odd Numbers
    print(
        "\nYour set contained no odd numbers."
        if len(odd_numbers) == 0
        else f"\nOdd :: {len(odd_numbers)} numbers\n\t::{odd_numbers}"
          ) 
        
    print(f"""
Your calculations:

Product\n\t:: {product}
Range\n\t:: {range_val}
Variance\n\t:: {variance:.2f}""")


def main():
    """Function to control the flow of the program.
    """
    num_list: list = get_positive_numbers()

    even_numbers, odd_numbers = separate_even_odd(num_list)

    unique_nums, duplicate_nums = remove_duplicates(num_list)
    
    display_results(
        num_list,
        unique_nums,
        duplicate_nums,
        even_numbers,
        odd_numbers,
        len(num_list),
        calculate_product(num_list),
        calculate_range(num_list),
        calculate_variance(num_list)
    )


# Call main on run
if __name__ == "__main__":
    main()