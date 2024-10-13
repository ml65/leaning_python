# Практическое задание по теме: "Словари и множества"

# Работа со словарями
my_dict = { "Ivan":2005, "Ann":2001, "Arina":2009, "Egor":2014}
print (my_dict)
print (my_dict["Ivan"], my_dict.get("Andrey"))
# my_dict["Masha"] = 2017
# my_dict["Sasha"] = 2021
my_dict.update({"Masha":2017,
                "Sasha":2021})
str = my_dict.pop("Ann")
print(my_dict)

# Работа с множествами
my_set = {"Мама",1,2.0, 1,1,1,1,1,2,2.0,True,(2,12,"жду"), 'Мама'}
print (my_set)
my_set.add(4)
my_set.add(5)
my_set.remove((2,12,"жду"))
print (my_set)


