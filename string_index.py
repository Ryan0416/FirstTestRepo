# 字串索引

credit_number = "1234-5678-9876-5432"
first_char = credit_number[0]
print("first character is :",first_char)

last_char = credit_number[-1]
print("last character is :",last_char)

# email分析 @前面使用者名稱 後面網域
email = "ryan@gmail.com"
index = email.find("@")
print("index is :",index)
print(email[:index])
print(email[index:])
print(email[(index+1):])