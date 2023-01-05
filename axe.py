# Axe
def axe(_x, _y):
    for y in range(_y):
        for x in range(_x):
            print(" #_#" * 10, end="")
    print()

axe(1,1)

# Pyramid
def pattern(rows):
    k = 2 * rows - 2
    for i in range(0, rows):
        for j in range(0, k):
            print(end=" ")
        k -= 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print()

pattern(8)

# number
def power(n1, n2):
    return n1, n2


base = int(input("Enter base number: "))
a = int(input("Enter power number(positive integer): "))

result = power(base,a)
print(base, "^", a,"=", result)

if (a != 0):
    base * power(base, a -1 )
else:
    pass

print(base,"^", a,"=", result)


