# Écrire un programme en python pour réviser ses tables de multiplication.
# Le programme tire 2 entiers au hasard et demande à l'utlisateur le produit.
# On interrogera 10 fois l'utilisatuer. +1pt par bonne et -1 sinon.

from random import *
score= 0
for i in range(10):
    a = randint(0, 10)
    b = randint(0, 10)
    c = int(input(str(a)+"*"+str(b)+"=?"))
    if a*b==c:
        score =score+1
        print("Bravo!, score="+str(score))
    else:
        score = score-1
        print("Faux, score="+ str(score))