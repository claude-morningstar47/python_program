# Écrire un programme pour calculer:

# on utlise la boucle for

def somme(a,b):
    s = 0
    for i in range(a,b):
        s = i + s
        # print(i, a)
    print("somme:",s)

# a- 1+2+3+...+1000
somme(1, 101)

def somme2(a,b):
    s = 0
    for i in range(a,b,2):
        s = i + s
        # print(i, a)
    print("somme:",s)

#1+3+5+...+99
somme2(1, 99)