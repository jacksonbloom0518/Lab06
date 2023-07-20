def decode_string(encoded_string): #this is a decoder function for Jackson's encoder
    decoded_string = ""             # starts with a string
    for char in encoded_string:
        if char.isdigit():          # checks each character in string if it is a digit or not
 
            decoded_digit = int(char) - 3  # digits get subtracted by 3

            if decoded_digit < 0:
                decoded_digit = decoded_digit + 10   # digits that are less than 0 get +10 (ex -2 goes to 8)

            decoded_string += str(decoded_digit)
        else:

            decoded_string += char

    return  decoded_string              # added decoded string in return so the decode method gives output





