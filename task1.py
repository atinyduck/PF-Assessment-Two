"""
Assessment 2

Hand-in by 09/01/2025 by 1600

By Jake Morgan
"""

# Function to prompt the user to input numbers. Checks should be perform so that the numbers are positive ints
def get_positive_numbers():
    positive_ints = []

    print("Please enter the amount of numbers you'd like to enter below.")
    input_amount: int = int(input("[]: "))

    # Loops the amount of times the user had input
    for i in range(input_amount):
        print("\nPlease enter a positive whole number.")

        # Loops until a correct input is present which breaks the loop
        while(True):  
            num_input: str = input("[]: ").strip()
            # If there is an input and its a positive integer, add it to the list
            if num_input != "" and int(num_input) >= 0:
                positive_ints.append(int(num_input))
                break
            else:
                print("Please enter a positive number.")

    return positive_ints

# Function to remove duplicates from the list, prints the duplicted numbers and returns a list with no duplicates
def remove_duplicates(numbers):
    unique_numbers = []

    for i in range(len(numbers)):
        if numbers[i] not in unique_numbers:
            unique_numbers.append(numbers[i])

    return unique_numbers

# Function to count the number of unique numbers
def count_unique_numbers(numbers):
    ammount_unique_nums: int = 0

    unique_numbers = remove_duplicates(numbers)

    for i in unique_numbers:
        ammount_unique_nums += 1

    return ammount_unique_nums

# Function to calculate the product of numbers
def calculate_product(numbers):
    nums_product: int = 0

    running_total: int = 1
    for i in numbers:
        running_total *= i

    return nums_product

# Function to calculate the range of numbers
def calculate_range(numbers):
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
def calculate_variance(numbers):
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
def separate_even_odd(numbers):
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
Your numbers had a product of {product}, a range of {range_val}, and a variance of {variance}.
    """

    print(long_text_one)

    print("Your set of unique numbers", *removed_duplicates, sep=", ")
    
    print("Your set of even numbers", *even_numbers, sep=", ")

    print("Your set of odd numbers", *odd_numbers, sep=", ")

    print(long_text_two)


# Main function to control the flow of the program
def main():
   
    numbers = get_positive_numbers()
    for num in numbers:
       print(f"{num},")

    even_numbers, odd_numbers = separate_even_odd(numbers)

    display_results(
        count_unique_numbers(numbers),
        remove_duplicates(numbers),
        even_numbers,
        odd_numbers,
        len(numbers),
        calculate_product(numbers),
        calculate_range(numbers),
        calculate_variance(numbers)
    )


# Call main on run
if __name__ == "__main__":
    main()