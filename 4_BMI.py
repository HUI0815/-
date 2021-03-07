


#4 BMI計算
Height = input("請輸入身高(公分)：")
Weight = input("請輸入體重(公斤)：")
BMI = float(Weight) / (float(Height)/100)**2
if (BMI < 18.5):
        print("BMI值為%.2f，體重過輕" % BMI)
elif (18.6 <= BMI and BMI < 24):
        print("BMI值為%.2f，正常範圍" % BMI)
elif (24 <= BMI and BMI < 27):
        print("BMI值為%.2f，稍重" % BMI)
elif (27 <= BMI and BMI < 30):
        print("BMI值為%.2f，輕度肥胖" % BMI)
elif (30 <= BMI and BMI < 35):
        print("BMI值為%.2f，中度肥胖" % BMI)
else:
        print("BMI值為%.2f，重度肥胖" % BMI)
