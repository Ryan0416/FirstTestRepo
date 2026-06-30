
goods=[]
prices=[]

while True:
    good = input("pls enter your goods:")
    if good.lower() == "q":
        break
    price = float(input(f"pls enter {good} price:"))
    goods.append(good)
    prices.append(price)
    # print("商品", goods)
    # print("價格", prices)
for index, good in enumerate(goods):
    # print("index: ", index)
    # print("name: ", good)
    print(f"第{ index+1} 商品是{good}，價格是{prices[index]:.2f} ")
total = sum(prices)
print(f"總價為:${total:.2f}")


