'''
Lab 6
Authors: Laura Garcia, Luna Prado
Class: COP3502C
Section: 22282
Description: Using Github and terminal to edit lab partner's code
'''
def encode(password):
    list = []
    for i in range(0, len(password)):
        list.append(password[i])
    for i in range(0, len(list)):
        list[i] = str(int(list[i]) + 3)
    return "".join(list)
def main():
    continue_program = True
    while continue_program:
        print("Main Menu")
        print("---------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        user_choice = input("Please enter an option: ")
        if user_choice == '1':
            user_pass = input("Please enter your password to encode: ")
            encoded_pass = encode(user_pass)
            print("Your password has been encoded and stored!")
        if user_choice == '2':
            encoded_pass = encode(user_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {user_pass}.")
        if user_choice == '3':
            break


if __name__ == '__main__':
    main()
