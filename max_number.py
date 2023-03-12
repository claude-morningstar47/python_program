# Define a function that takes a list of numbers as input
# and returns the maximum number
from abc import ABC, abstractmethod


def get_max_number(numbers):
    # Initialize a variable to hold the maximum number
    max_number = numbers[0]

    # Loop through the list of numbers
    for number in numbers:
        # If the current number is greater than the current maximum number,
        # update the maximum number
        if number > max_number:
            max_number = number

    # Return the maximum number
    return max_number


# Test the function with some numbers
print(get_max_number([1, 2, 3, 4, 5]))  # should print 5
print(get_max_number([100, 200, 300, 400, 500]))  # should print 500
print(get_max_number([-1, -2, -3, -4, -5]))  # should print -1


print("-----------------------------------------")


class Payement(ABC):
    def print_slip(self, amount):
        print('Purchase of amount: ', amount)

    @abstractmethod
    def payement(self, amount):
        print("Credit card payement of: ", amount)
        # pass

    def payement_2(self, amount):
        print("Credit card payement_2 of: ", amount)


class CreditCardPayement(Payement):
    def payement(self, amount):
        # print("Credit card payement of: ", amount)
        return super().payement(amount)


class Credit(Payement):
    def payement(self, amount):
        return super().payement_2(amount)


obj = CreditCardPayement()
obj_2 = Credit()

obj.payement(100)
obj.print_slip(100)

obj_2.payement(200)
obj_2.print_slip(200)
print(isinstance(obj, Payement))
