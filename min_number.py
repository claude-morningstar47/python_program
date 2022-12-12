# define a list of numbers
numbers = [11, 920, 830, 540, 50]

# initialize the minimum number to the first number in the list
min_num = numbers[0]

# iterate over the numbers in the list
for num in numbers:
  # if the current number is less than the current minimum, update the minimum
  if num < min_num:
    min_num = num

# print the minimum number
print(min_num)
