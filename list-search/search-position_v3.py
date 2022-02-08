number_list = [11, 12, 14, 3, 7, 13, 14, 11, 8, 9]
searched_element = 14

for i in range(len(number_list)):
    if number_list[i] == searched_element:
        el_position = i
        print("Шуканий елемен є під номером: ", el_position)
