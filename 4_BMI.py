


#4 BMI計算
height=eval(input('请键入您的身高(m):'))
weight=eval(input('请键入您的体重(kg):'))

BMI=float(float(weight)/(float(height)**2))
#公式
if BMI<=18.4:
    print('身體狀態：','偏瘦')
elif BMI<=23.9:
    print('身體狀態：','正常')
elif BMI<=27.9:
    print('身體狀態：','超重')
elif BMI>=28:
    print('身體狀態：','肥胖')
