# def hello(greeting, title, first_name, last_name):
#     print(f"{greeting} ,{title}, {first_name}, {last_name}")
#
# # hello("你好!", "MR", "Ryan", "Liu" )
# hello(greeting="你好!",title="MR", first_name="Fandy", last_name="Sung" )

#獲得電話號碼
def phone_number(country_code, area_code, first, last):
    return f"{country_code}-{area_code}-{first}-{last}"

result = phone_number(country_code="886", area_code="02", first="1234", last="5678")
print(result)


