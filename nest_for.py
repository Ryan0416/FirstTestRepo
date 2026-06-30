#巢狀迴圈
# for x in range(1,10):
#     print(x,end=" ")
# for y in range(5):
#     for x in range(1,10):
#         print(x,end=" ")
#     print()#加上這個他會換行
rows = int(input("pls enter number of rows: "))
cols = int(input("pls enter number of columns: "))
symbol = input("pls enter symbol: ")
for row in range(rows):
    for col in range(cols):
        print(symbol, end=" ")
    print()
