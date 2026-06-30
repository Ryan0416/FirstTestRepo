# try:
#     x = int(input("輸入一個整數"))
#     y = int(input("輸入另一個整數"))
#     print(x/y)
# except ValueError:
#     print("請輸入整數")
# except ZeroDivisionError:
#     print("除數不能為0")


#只抓錯誤
try:
    x = int(input("輸入一個整數"))
    y = int(input("輸入另一個整數"))
    print(x/y)
except (ValueError,ZeroDivisionError):
    print("出現錯誤，請重新輸入")
else:
    print("Else")
# finally:#不論怎樣都會執行
#     print("無論是否出現異常，都會執行")



