
def encode(inputted_password):
    encoded_password = []
    for j in inputted_password:
        i = int(j)
        i += 3
        encoded_password.append(i)
    return encoded_password

def decode(encoded_password):
    decoded_password = []
    for j in encoded_password:
        i = int(j)
        i -= 3
        decoded_password.append(i)
    return decoded_password

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        menu_selection = int(input("Please enter an option: "))

        if menu_selection == 1:
            inputted_password = list(input("Please enter your password to encode: "))
            encoded_password = encode(inputted_password)
            encoded_string = ''.join(map(str, encoded_password))
            print("Your password has been encoded and stored!")

        if menu_selection == 2:
            if 'encoded_string' in locals():
                decoded_password = decode(list(encoded_string))
                decoded_string = ''.join(map(str, decoded_password))
                print(f'The encoded password is {encoded_string}')
                print(f'The decoded password is {decoded_string}')
            else:
                print("No password encoded yet.")

        if menu_selection == 3:
            exit()

if __name__ == '__main__':
    main()
