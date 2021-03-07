#8__油箱公升數，95每公升:21.6元，98每公升：23.4元，求加95或98分別要多少才能加滿

gasoline = int(input('汽車油箱公升數：'))

a = gasoline * 21.6
b = gasoline * 23.4
print("95加滿要：${}元，98加滿要：${}元".format(a,b))
