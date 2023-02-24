# def gen_number():
#     for i in range(1,10000):
#         phone_number = "+336021"+ str(i+1000).zfill(5)
#         print(f"{i}/{phone_number}")

def gen_number():
    phone_number = "+336021"
    for i in range(1,1000):  
        phone_number+= str(i+1000).zfill(5)
        yield phone_number

for number in gen_number():
    print(number)



import unittest

class TestGenNumber(unittest.TestCase):
    def test_gen_number(self):
        self.assertEqual(gen_number(), "+3360211000")
        self.assertEqual(gen_number(), "+3360212001")
        #etc

if __name__ == '__main__':
    unittest.main()
