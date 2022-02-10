
number_list = [11, 12, 14, 3, 7, 13, 14, 11, 8, 9]
searched_el = int(input("Який елемент знайти? "))
positions_search = []
count = 0
for el in number_list:
    count += 1
    if el == searched_el:
        positions_search.append(count -1)
print(f"Елемент {searched_el} є в сиску на позиціях {positions_search}")