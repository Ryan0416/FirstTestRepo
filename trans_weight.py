weight = float(input("tell me your weight or temperture: "))
amount = input("你的體重是公斤還是磅?(kg/lb), or 轉換溫度 c or f")


operations = {
    "kg": lambda weight: weight *2.2,
    "lb": lambda weight: weight / 2.2,
    "c": lambda weight: 9*weight/5+32,
    "f": lambda weight: weight-32,
}

result = operations[amount](weight)

if amount == "kg" :
    print(f"你的磅數是:{result:.2f}磅")
elif amount == "lb" :
    print(f"你的公斤數是:{(result, 2)}公斤")
elif amount == "c" :
    print(f"華氏溫度為:{result}度")
elif amount == "f" :
    print(f"攝氏溫度為{result}")
else :
    print("error input")



