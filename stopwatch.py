import time
# time.sleep(1)
#倒數
# time_set = int(input("輸入倒數計時秒數:"))
#
# for x in range(time_set, 0, -1):
#     seconds = x%60
#     minutes = x//60%60
#     print(f"{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("時間到了!!!!")


#正數(從1開始)
time_set = int(input("輸入計時秒數:"))

for x in range(1,time_set+1):
    seconds = x%60
    minutes = x//60%60
    print(f"{minutes:02}:{seconds:02}")
    time.sleep(1)
print("時間到了!!!!")