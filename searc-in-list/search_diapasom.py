
number_list = [11, 12, 14, 5.5, 3, 7, 13, 14, 11, 8, 9, 12, 155]

searched_el = []
searched_pos = []
for i in range(len(number_list)):
    if number_list[i] > 5 and number_list[i] < 10:
        searched_el.append(number_list[i])
        searched_pos.append(i)
print(searched_el)
print(searched_pos)

# print(len("Богданко"))