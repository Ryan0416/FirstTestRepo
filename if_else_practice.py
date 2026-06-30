#if else elif

#boolean
for_sale = False
if for_sale:
    print("正在出售")
else:
    print("not sales")

#if else
# age = int(input("please enter your age:"))
# if age >= 18:
#     print("you good to registed")
# else:
#     print("you are not registered")

age = int(input("enter your age:"))
if age >= 100:
    print("you cannot registed")
elif age >= 18:
    print("you are eligible")
elif age < 0:
    print("you are not born")
else:
    print("you are eligible for registeration until 18")
