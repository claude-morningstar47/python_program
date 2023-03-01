# On dispose d'une feuille de papier d'épaisseur 0,1 mm.
# Combien de fois doit-on la plier au mininmun pour que l'épaisseur dépasse la hauteur de la tour Eiffel 325 m.
# Écrire un programme en Python pour résoudre ce problème.

ep = 0.1
p = 0

while(ep <= 340000):
    p = p + 1
    ep = ep * 2
    # print(p, ep)
print("Nombre:",p)