def sort_clothing(clothing_data, sort_choice):

    if sort_choice == 1:
        sorted_data = sorted(clothing_data.items(), key=lambda x: x[1][0])
    elif sort_choice == 2:
        sorted_data = sorted(clothing_data.items(), key=lambda x: x[1][1])
    else:
        sorted_data = sorted(clothing_data.items(), key=lambda x: x[1][2])
    return sorted_data
