
friend_names = ["Маша", "Петя", "Коля", "Марина", "Маша"]
user_name = input("Як тебе звати: ")
# if user_name in friend_names:
#     print("О! Ти в списку моїх друзів")
# else:
#     print("Нажаль, ми з тобою ще не подружились")


number_friend = []
count = 1
for el in friend_names:
    count += 1
    if el == user_name:
        number_friend.append(count -1)
print(f"{user_name} ти є в сиску моїх друзів на {number_friend} місці")