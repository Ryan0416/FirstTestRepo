import math

num1 = float(input("輸入第一個數字"))
operator = input("輸入運算符號")
num2 = float(input("輸入第二個數字"))

operations ={
    "+": lambda num1, num2: num1 + num2,
    "-": lambda num1, num2: num1 - num2,
    "*": lambda num1, num2: num1 * num2,#有點類似def 問chat gpt叫她解釋他會說
    "/": lambda num1, num2: num1 / num2,
}
result = operations[operator](num1, num2)
# print(operations)
# print(operator)
# print(num1, num2)
print(round(result,4))