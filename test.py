import builtins

# function = [i for i in dir(builtins) if i[0].islower]

# fmt = ' {:18s} '*4

# for fn in zip(*[iter(function)]*4):
#     print(fmt.format(*fn))

# une fonction tres delicate
functions = [func for func in dir(builtins) if callable(
    getattr(builtins, func)) and func[0].islower()]

# Vérifier si la dernière tranche de la liste contient moins de 4 éléments
last_slice = len(functions) % 4
if last_slice != 0:
    # Ajouter des éléments nuls à la dernière tranche pour avoir une taille de 4
    functions.extend([''] * (4 - last_slice))

# Afficher les noms des fonctions dans des colonnes formatées
for i in range(0, len(functions), 4):
    print('{:20s}{:20s}{:20s}{:20s}'.format(*functions[i:i+4]))


def findMaxConsecutiveOnes(nums: list[int]) -> int:
    start = 0
    end = 0
    max_len = 0

    while end < len(nums):
        if nums[end] == 0:
            max_len = max(max_len, end - start)
            start = end + 1
        end += 1
    max_len = max(max_len, end - start)

    return max_len


print(findMaxConsecutiveOnes(
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]))
