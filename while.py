#while迴圈

# name = input("pls enter your name: ")
# if name == "":
#     print("please enter your name")
# else:
#     print(f"Hello {name}")


# while name == "":
#     name = input("pls enter your name: ")
# print(f"Hello {name}")

# Food = input("pls enter your favorite Food: ")
# while Food != "q":
#     print("please enter your favorite Food")
#     Food = input("pls enter your favorite Food: ")
# print("Good bye")

number = int(input("pls enter 1-10: "))
while number >= 10 or number <= 1:
    print("your enter number is out of range")
    number = int(input("pls enter 1-10: "))
print(f"Your number is {number}")