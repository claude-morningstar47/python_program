for i in range(2):
    print("ok", i+1)


my_list = [1,2,3]
for item in my_list:
    print(item)

my_dict  = {1:'one', 2:'two', 3:'three'}
for key in my_dict:
    print( key, my_dict[key])


for i, item in enumerate(my_list):
    my_list[i] = item**2 
    print(my_list)


import urllib.request, json
resp = urllib.request.urlopen('https://query2.finance.yahoo.com/v10/finance/quoteSummary/tsla?modules=price')
data = json.loads(resp.read())
price = data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
print(price)