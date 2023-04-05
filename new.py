import time

a = " HELLO je suis le chatiment"
n = len(a)

for i in range(n):
    time.sleep(1000)
    print(a[i], end="")
