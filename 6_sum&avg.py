#華輸入全班5位同學成績，求總成績及平均
A=float(input('A同學成績:'))
B=float(input('B同學成績:'))
C=float(input('C同學成績:'))
D=float(input('D同學成績:'))
E=float(input('E同學成績:'))
#總成績計算
sum=A+B+C+D+E
# 平均成績
avg = sum/5
print("總分：{}分，平均：{:.2f}分".format(sum, avg))

     
