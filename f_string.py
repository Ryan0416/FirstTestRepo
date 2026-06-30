#字串格式化
price_1 = 3.321
price_2 = -77
price_3 = 15.11



#小數點的精確度
# print(f"價格1為 {price_1:.2f}\n"
#       f"價格2為 {price_2:.2f}\n"
#       f"價格3為 {price_3:.2f}")
#加上正負
print(f"價格1為 {price_1:+.2f}\n"
      f"價格2為 {price_2:+.2f}\n"
      f"價格3為 {price_3:+.2f}")
#對齊 < > ^
print(f"價格1為 {price_1:<10.2f}\n"
      f"價格2為 {price_2:^10.2f}\n"
      f"價格3為 {price_3:>10.2f}")
#混合不同符號
print(f"價格1為 {price_1:>+.2f}\n"
      f"價格2為 {price_2:>+.2f}\n"
      f"價格3為 {price_3:>+.2f}")
