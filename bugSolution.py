def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

# Example usage demonstrating the solution:
my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}")  # Output: 0
my_numbers = [1, 2, 3, 4, 5]
result = calculate_average(my_numbers)
print(f"The average is: {result}")  # Output: 3.0
my_numbers = [1, 2, 'a', 4, 5]
result = calculate_average(my_numbers) #This will not throw error and print 3.0
print(f"The average is: {result}") 