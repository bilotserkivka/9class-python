
names = ["Богдан", "Олександра", "Максим", "Дарина", "Олександр", "Тетяна", "Свидригайло", "Bob", "Мася"]

long_names = []
for name in names:
    if len(name) == 6:
        long_names.append(name)

print(long_names)

names_with_o = []
for n in names:
    if "о" in n or "О" in n:
        names_with_o.append(n)
print(names_with_o)

names_with_o = []
for n in names:
    if "о" in n.lower():
        names_with_o.append(n)
print(names_with_o)
