#in後面要接可迭代
# for x in range(1,11):
#     print(x)
#
# for x in reversed(range(1,11)):
#     print(x)
# print("Happy New Year")
#
# card_num = "1234-5678-9012-3456"
# for x in card_num:
#     if x == "9":
#         # continue
#         break
#     else:
#         print(x,end="")

#字典
#key: value
my_dict = {"a":1,"b":2,"c":3}
for key, value in my_dict.items():
    print("key:",key)
    print("value:",value)
