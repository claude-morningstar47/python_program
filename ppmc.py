from re import A
import string


def askforint():
    a = ""
    while not isinstance(a, int):
        a = input("un entier ?")
        try:
            a = int(a)
        except:
            print("il faut un entier")
    return a

def PGCD(a, b):
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b

def PPMC(a, b):
    return a * b// PGCD(a, b)


a = askforint()
b = askforint()
p = PGCD(a, b)
print("pgcd=", p)
p = PPMC(a,b)
print("ppmc=", p)

string = input("ok?")