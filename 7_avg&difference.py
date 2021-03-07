#7__求3次成績的平均及第一次考試與平均之差
a = float(input('第一次多益分數:'))
b = float(input('第二次多益分數:'))
c = float(input('第三次多益分數:'))
#三次考試平均
avg = (a+b+c)/3
#第一次考試與平均之差
difference = avg-a
print("平均：{}分，第一次考試與平均之差：{}分".format(avg,difference))
