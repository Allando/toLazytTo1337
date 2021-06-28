



def main():
    

    clearText = input("Input ya value: ")
    
    print(converter(clearText))



def converter(input_string):
    converted_letters = ""

    # print(input_string)

    for letter in input_string:
        # print(letter)
        if letter.lower() == 'a':
            converted_letters = converted_letters + '4'
        elif letter.lower() == 'b':
            converted_letters = converted_letters + '8'
        elif letter.lower() == 'e':
            converted_letters = converted_letters + '3'
        elif letter.lower() == 'g':
            converted_letters = converted_letters + '9'
        elif letter.lower() == 'l':
            converted_letters = converted_letters + '1'
        elif letter.lower() == 'o':
            converted_letters = converted_letters + '0'
        elif letter.lower() == 's':
            converted_letters = converted_letters + '5'
        elif letter.lower() == 't':
            converted_letters = converted_letters + '7'
        else:
            converted_letters = converted_letters + letter

    return converted_letters


# abcdefghijklmopqpurstuvwxyz
# 48--3-9----1-0-----57------

main()
