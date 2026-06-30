#args => arguments任意數量的參數 * tuple是一種內建的資料結構，用來儲存多個項目。它最大的特點是有序且不可變（Immutable），一旦建立就無法新增、刪除或修改裡面的元
#kwargs => 關鍵字 + args (keyword args)

# def add(a, b):// 無法加三個value
#     return a + b
# print(add(1, 2))

def add(*args):
    total = 0
    for arg in args:
        print(f"arg: {arg}")
        total += arg
    return total

print(add(1,2,3,4,5))

#關鍵字+args // kwargs = 字典刑事 可以傳入任意數量參數

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"key: {key}  value: {value}")

print_info(name="Alice",age="25", occupation="engineer")