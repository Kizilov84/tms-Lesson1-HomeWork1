# задание №1 "создать 3 переменных с одинаковыми данными с одинаковыми идентификаторами"
city = "minsk"
hero_City = "minsk"
the_capital_of_country = "minsk"
print(id(city)) == print(id(hero_City)) == print(id(the_capital_of_country))

# задание №2 "Создать 2 перменных с одинаковыми данными с разными идентификаторами"
money1 = ["rubles"]
money2 = ["rubles"]
print(id(money1)) == print(id(money2))

# задание №3 "поменять их типы так, чтобы у 1х трех были разные идентификаторы,
#а у 2х последних были одинаковые"
city = "minsk"
hero_City = ["minsk"]
the_capital_of_country = ["minsk"]
print(id(city)) == print(id(hero_City)) == print(id(the_capital_of_country))

money1 = "rubles"
money2 = "rubles"
print(id(money1)) == print(id(money2))