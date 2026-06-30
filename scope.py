#作用域
#local 區域
#enclose
#global 全域
#built-in

#變數範圍
# a = 10
# def fun1():
#     a = 1
#     print("a:",a)
#
#     def fun2():
#         b = 2
#         print("b:", b)
#         print("a:", a)
#     fun2()
#
# fun1()

#built-in
from math import e
print(e)

def fun1():
    print(e)
    print(round(e))

fun1()
