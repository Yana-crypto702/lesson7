#Словарь
my_dict={"Yana":2004, "Dasha":2005}
print(my_dict)
print(my_dict["Yana"])
print(my_dict.get("Olga",))
my_dict.update({"Valya":2003, "Nadya":2002})
a= my_dict.pop("Yana")
print(a)
print(my_dict)
#Множество
my_set={1,1,2,1,2, 'Яблоко', 42.314}
print(my_set)
my_set.add(3)
my_set.add((5,6,1.6))
my_set.discard(1)
print(my_set)