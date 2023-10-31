def decoder(input_var):
    str_list = []
    for i in range(0, len(input_var)):
        str_list.append(input_var[i])
        str_list[i] = str(int(str_list[i]) - 3)
    final_list = "".join(str_list)
    return final_list
