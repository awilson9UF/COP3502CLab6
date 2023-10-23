
def encode(inputted_password, encoded_password):
    for j in inputted_password:
        i = int(j)
        i += 3
        encoded_password.append(i)
    return encoded_password


def main():
    #main loop to keep the code running until quit
    while True:

        #prints the menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        #takes inputted menu option
        menu_selection = int(input("Please enter an option: "))

        #runs statements for menu selection 1
        if menu_selection == 1:
            inputted_password = list(input("Please enter your password to encode: "))
            encoded_password = []
            print("Your password has been encoded and stored!")
            #makes the encoded password a string
            encoded_string = ''.join(map(str, encode(inputted_password, encoded_password)))

        #runs statements for decoder, needs to be FIXME
        if menu_selection == 2:

            #final print statement
            print(f'The encoded password is {encoded_string}') #FIXME finish the print statement with decoder

        #exits if 3 is selected
        if menu_selection == 3:
            exit()


#runs the program
if __name__ == '__main__':
    main()
