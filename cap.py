
# def closest(ts):
#     min1=abs(ts[0])

#     for i in ts:
#         if(abs(i)<abs(min1)):
#             min1=i
#     print("Closest to zero for array 1: "+ str(min1))

def closest(ts):
    min1=abs(ts[0])

    for i in ts:
        if(abs(i)<abs(min1)):
            min1=i
    print("Closest to zero in array: "+ str(min1))

array_1 = [5, 3.2, -1.2, -0.2, 7]
array_2 = [19, -20, -4.7, 6, 9, 42]
array_3 = [4, 0.3, -9, 8, 6, 14]

closest(array_3)