#list 多值存到變數中

# fruits = ["apple", "banana", "cherry", "pineapple"]
# print(fruits[0])

# for f in fruits:
#     print(f)
# fruits.append("orange") #加入在[]最後面
# print(fruits)
#
# fruits.remove("orange") #刪除
# print(fruits)

# print(fruits.index("pineapple")+1) #這樣可以讓輸出變1

# fruits.append("apple")
# fruits.append("apple")
# print(fruits.count("apple"))
#
# fruits.reverse()
# print(fruits)

#--------------------------------------------------------------------------------
#set

# fruits_set = {"apple", "banana", "cherry"}
# # fruits_set.add("orange")
# # for fruit in fruits_set:
# #     print(fruit, end=" ")
# if "apple" in fruits_set:
#     print("have apple")
#
# if "pineapple" in fruits_set:
#     print("have pineapple")
# else:
#     print("have no pineapple")

# tuple元組 有順序且無法add
fruits_tuple = ("Apple", "Orange", "Orange", "Orange", "Grape", "pineapple")
# result = fruits_tuple.count("Orange")
# print(result)
result = fruits_tuple.index("pineapple")+1
print(result)