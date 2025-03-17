from typing import List

def find_numbers(numbers: List[int], divisible_by: int, not_multiple_of: int) -> str:
    """
    Finds all numbers in the given list that are divisible by `divisible_by`
    but not a multiple of `not_multiple_of`. Returns them as a comma-separated string.

    Args:
        numbers (List[int]): The list of numbers to check.
        divisible_by (int): The divisor to filter numbers that are divisible.
        not_multiple_of (int): The number that filtered numbers should not be a multiple of.

    Returns:
        str: A comma-separated string of valid numbers.
    """
    if not numbers:
        return ""  # Return empty string for an empty list

    # List comprehension for efficient filtering
    valid_numbers = [str(num) for num in numbers if num % divisible_by == 0 and num % not_multiple_of != 0]

    return ",".join(valid_numbers)  # Join the numbers as a single string


if __name__ == "__main__":
    # Define the range of numbers to check
    numbers_range = list(range(2000, 3201))

    # Set conditions: Divisible by 7 but not a multiple of 5
    result = find_numbers(numbers_range, divisible_by=7, not_multiple_of=5)

    # Print the result to standard output
    print(result)
