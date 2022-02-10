
number_list = [11, 12, 14, 3, 7, 13, 14, 11, 8, 9]
searched_el = int(input("Який елемент знайти? "))

el_positions = []
for i in range(len(number_list)):
    if number_list[i] == searched_el:
        el_positions.append(i)

print(f"Eлемен {searched_el} є під номерaми:  {el_positions}")
