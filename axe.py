# axe
def axe(_x, _y):
    for y in range(_y):
        for x in range(_x):
            print(" #_#" * 10, end="")
    print()

axe(1,1)

def pattern(rows):
    k = 2 * rows - 2
    for i in range(0, rows):
        for j in range(0, k):
            print(end=" ")
        k -= 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print()

pattern(5)