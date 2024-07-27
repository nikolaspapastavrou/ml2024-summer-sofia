# Get the number of numbers to read
number_of_numbers = input("Please type the number of numbers you are going to read\n")
# Validate input
assert number_of_numbers.isnumeric and number_of_numbers[0] != "0", "The number must be a positive integer"
# Convert to int so we can read that many numbers
number_of_numbers = int(number_of_numbers)

input_numbers = []

for i in range(number_of_numbers):
    # Read current number
    input_number = input("Please type the current number to read\n")
    # Validate current number
    assert (input_number.isnumeric and input_number[0] != "0") or (input_number[0] == "-" and input_number[1:].isnumeric) or input_number == "0", "The number must be an integer"
    # Append current number in read numbers
    input_numbers.append(input_number)

number_to_find_index = input("Please type the number to find the index of\n")
# Validate the number to find the index of
assert (number_to_find_index.isnumeric and number_to_find_index[0] != "0") or (number_to_find_index[0] == "-" and number_to_find_index[1:].isnumeric) or number_to_find_index == "0", "The number must be an integer"

# If the number to find the index of does not exist, output -1. Othewise, output the index of the number + 1
if number_to_find_index not in input_numbers:
    print(-1)
else:
    print(input_numbers.index(number_to_find_index)+1)
