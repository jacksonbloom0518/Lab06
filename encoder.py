def encode_string(string):           
    encoded_string = ""
    for char in string:
        if char.isdigit():

            encoded_digit = int(char) + 3

            if encoded_digit > 9:
                encoded_digit = encoded_digit % 10

            encoded_string += str(encoded_digit)
        else:
  
            encoded_string += char

    return encoded_string


def decode_string(encoded_string):
    decoded_string = ""
    for char in encoded_string:
        if char.isdigit():
 
            decoded_digit = int(char) - 3

            if decoded_digit < 0:
                decoded_digit = decoded_digit + 10

            decoded_string += str(decoded_digit)
        else:

            decoded_string += char

    return decoded_string


encoded_result = None

# you should put this in the code in order to separate the methods from the displayed / run part of the program (and indent accordingly) 
# if __name__ == '__main__':

while True:
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

    option = input('Please enter an option: ')

    if option == '1':
        input_string = input('Please enter the string you want to encode: ')
        encoded_result = encode_string(input_string)
        print('Your password has been encoded and stored!')

    elif option == '2':
        if encoded_result is not None:
            decoded_result = decode_string(encoded_result)
            print(f'The encoded password is {encoded_result}, and the original password is {decoded_result}.')
        else:
            print('Sorry, need to encode a password first')

    elif option == '3':
        break
    else:
        print('Invalid option. Please choose again.')
