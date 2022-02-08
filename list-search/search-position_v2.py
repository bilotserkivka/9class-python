number_list = [11, 12, 14, 3, 7, 13, 14, 11, 8, 9]
searched_element = 14

el_positions = []
for i in range(len(number_list)):
    if number_list[i] == searched_element:
        el_positions.append(i)

print("Шуканий елемен є під номерaми: ", el_positions)
