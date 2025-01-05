
# Function to prompt the user to input numbers. Checks should be perform so that the numbers are positive ints
def get_positive_numbers() -> list:
    """Function to ask the user to enter a specified amount of integers.

    Returns:
        list: The list of entered numbers from the user.
    """
    
    positive_ints = list()

    print("Please enter the amount of numbers you'd like to enter below.")
    while True:
        try:
            input_amount: int = int(input("[]: ").strip())
            break
        except:
            print("Please enter a valid integer.")
        
    # Loops the amount of times the user had input
    for _ in range(0, input_amount):
        print("\nPlease enter a positive whole number.")

        # Loops until a correct input is present which breaks the loop
        while True:  
            # If there is an input and its a positive integer, add it to the listenter a positive number.")
            try:
                num_input: int = int(input("[]: ").strip())
                positive_ints.append(num_input)
                break
            except:
                print("Please enter a valid integer.")

    return positive_ints

# Function to remove duplicates from the list, prints the duplicted numbers and returns a list with no duplicates
def remove_duplicates(numbers: list) -> list:
    """Takes the users entered numbers as a parameter and removes any duplicate numbers
    from the list.

    Args:
        numbers (list, optional): The user's entered numbers.

    Returns:
        list: The list of only unique numbers.
    """
    unique_numbers = list()

    # Loops through the numbers list and checks if the number is in unique numbers if not it'll add it.
    for i in range(len(numbers)):
        if numbers[i] not in unique_numbers:
            unique_numbers.append(numbers[i])
        else:
            print(f"Duplicate: Removed {numbers[i]}")

    return unique_numbers

# Function to count the number of unique numbers
def count_unique_numbers(numbers: list) -> int:
    """Counts the amount of unique numbers in the users given list.

    Args:
        numbers (list, optional): The user's entered numbers.

    Returns:
        int: The amount of unique numbers.
    """
    ammount_unique_nums: int = 0

    unique_numbers = remove_duplicates(numbers)

    for _ in unique_numbers:
        ammount_unique_nums += 1

    return ammount_unique_nums

# Function to calculate the product of numbers
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

# Function to calculate the range of numbers
def calculate_range(numbers: list) -> int:
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

# Function to calculate the variance of numbers
def calculate_variance(numbers: list) -> int:
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

# Function to separate even and odd numbers
def separate_even_odd(numbers: list) -> list:
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

# Function to display the results
def display_results(unique_numbers, removed_duplicates, even_numbers, odd_numbers, count, product, range_val, variance):
    
    long_text_one = f"""
Your results:

You entered a total of {count} numbers, containing {unique_numbers} unique numbers.
There are {len(even_numbers)} even and {len(odd_numbers)} odd numbers.
    """

    long_text_two = f"""
Your numbers had a product of {product}, 
a range of {range_val}, 
and a variance of {"{:.2f}".format(variance)}.
    """

    print(long_text_one)

    if len(removed_duplicates) == 0:
        print("Your set contained no unqiue numbers.")
    else:
        print(f"Your set of unique numbers: {removed_duplicates}")
    
    if len(even_numbers) == 0:
        print("Your set contained no even numbers.")
    else:
        print(f"Your set of even numbers: {even_numbers}")

    if len(odd_numbers) == 0:
        print("Your set contained no odd numbers.") 
    else:
        print(f"Your set of odd numbers: {odd_numbers}")

    print(long_text_two)


# Main function to control the flow of the program
def main():
    num_list: list = get_positive_numbers()
    print(*num_list,)

    even_numbers, odd_numbers = separate_even_odd(num_list)

    display_results(
        count_unique_numbers(num_list),
        remove_duplicates(num_list),
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