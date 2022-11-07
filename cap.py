
# def closest(ts):
#     min1=abs(ts[0])

#     for i in ts:
#         if(abs(i)<abs(min1)):
#             min1=i
#     print("Closest to zero for array 1: "+ str(min1))

def closest(ts):
    min1=abs(ts[0])

    for i in ts:
        if(abs(i)<abs(min1)):
            min1=i
    print("Closest to zero in array: "+ str(min1))

array_1 = [5, 3.2, -1.2, -0.2, 7]
array_2 = [19, -20, -4.7, 6, 9, 42]
array_3 = [4, 0.3, -9, 8, 6, 14]

closest(array_3)

# Class and methods
class Person:
    def __init__(self, name, sex, profession) -> None:
        # data members (instance variable)
        self.name = name
        self.sex = sex
        self.profession = profession

    # Behavior (instance methods)
    def show(self):
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

    # Behavior (instance methods)
    def work(self):
        print(self.name, 'working as a', self.profession)


# Create object of a class
person = Person('Mops', 'Male', 'Software Engineer')

# Call methods
person.show()
person.work()