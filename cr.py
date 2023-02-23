# from random import *
# import os

# u_pwd = input("Enter a password: ")
# pwd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '1','2','3','4','5','6']

# pw=""
# while(pw!=u_pwd):
#     pw=""
#     for i in range(len(u_pwd)):
#         guess_pwd = pwd[randint(0,17)]
#         pw=str(guess_pwd)+str(pw)
#         print(pw)
#         print("Cracking Password...Please")
#         os.system("clear")
# print("Your Password Is :" ,pw)


# from random import *
# import os

# u_pwd = input("Enter a password: ")
# pwd = set('abcdefghijklmnopqrstuvwxyz123456')

# pw=""
# while(pw!=u_pwd):
#     pw=""
#     for i in range(len(u_pwd)):
#         guess_pwd = choice(list(pwd))
#         pw=str(guess_pwd)+str(pw)
#         print(pw)
#         print("Cracking Password...Please")
#         os.system("clear")
# print("Your Password Is :" ,pw)


from random import *
import os

u_pwd = input("Enter a password: ")
pwd = list('abcdefghijklmnopqrstuvwxyz123456')

pw=""
while(pw!=u_pwd):
    pw=""
    for i in range(len(u_pwd)):
        guess_pwd = pwd[randint(0, len(pwd) - 1)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print("Cracking Password...Please")
        os.system("clear")
print("Your Password Is :" ,pw)
