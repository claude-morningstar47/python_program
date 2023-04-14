import time

a = " HELLO MORNINGSTAR, Notez que le code JavaScript utilise setTimeout pour simuler l'effet de la fonction Sleep de Windows.h. De plus, il utilise process.stdout.write plutôt que console.log pour permettre l'impression des caractères sur la même ligne. "
n = len(a)

for i in range(n):
    time.sleep(0.1)
    print(a[i], end="", flush=True)
