import math

#無條件進位 捨去
x = 9.5
print(round(x))
print(math.ceil(x))#無條件進位
print(math.floor(x))#無條件捨去
#圓周率
print(math.pi)

#計算圓的周長 2piR
radius = float(input("請輸入圓半徑"))
perimeter = 2 * math.pi * radius
print(round(perimeter, 2)) #2表示顯示到第二位

#計算圓的面積 piR平方
radius = float(input("請輸入圓半徑"))
circle = (radius ** 2) * math.pi
print("圓面積:", round(circle, 2))