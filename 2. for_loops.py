user_input = ""

while user_input != 'end' :
    user_input = input(">>")
    if user_input == 'n':
        continue
    elif user_input == 'j':
        break
    print(user_input)