import random

import pyautogui as pg

import time

animal =("monkey","donkey", "dog")

time.sleep(8)

for i in range(23):
    a = random.choice(animal)
    pg.write("you are a" + a)
    pg.press('enter')
    

#! Single number
def single_number():
    count = 0
    for i in nums:
        count = count * i
        return count

nums = [4,5,3,1,2]
print(single_number())