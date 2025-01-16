def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage (contains the bug):
my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will print 0 as expected
my_numbers = [1, 2, 3, 4, 5]
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will print 3.0 as expected
my_numbers = [1, 2, 'a', 4, 5] #this will throw an error
result = calculate_average(my_numbers)
print(f"The average is: {result}")