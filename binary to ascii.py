import time

def blank_page():
    for i in range(0,100):
        print()
    return

def report_error(message):
    blank_page()
    print('-{:^50}-'.format(message))
    time.sleep(1)
    return

def display_menu():
    blank_page()
    print('{:^50}'.format('1 - ASCII to Binary'))
    print('{:^50}'.format('2 - Binary to ASCII'))
    print('{:^50}'.format('3 - Quit           '))
    return

def invalid_choice():
    blank_page()
    report_error('Invalid Choice')
    time.sleep(1)
    blank_page()
    return

def start():
    Letter = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']    
    Binary = ['00100000','01000001','01000010','01000011','01000100','01000101','01000110','01000111','01001000','01001001','01001010','01001011','01001100','01001101','01001110','01001111','01010000','01010001','01010010','01010011','01010100','01010101','01010110','01010111','01011000','01011001','01011010']

    program_end = False
    while not program_end:
        display_menu()
        menu_option = get_menu_option()
        if menu_option == 1:
            ascii_to_binary(Letter, Binary)
        elif menu_option == 2:
            binary_to_ascii(Letter, Binary)
        elif menu_option == 3:
            program_end = True
        else:
            invalid_choice()

def input_phrase():
    check = False
    while check == False:
        phrase = input('ASCII: ')

        if phrase == '':
            report_error('Phrase cannot be blank')
        else:
            check = True
            return phrase

def get_menu_option():
    print()
    check = False
    while check == False:
        try:
            menu_option = int(input('Enter a number: '))
            check = True
        except:
            blank_page()
            report_error('Invalid Data Type')
            blank_page()
            display_menu()
            
    if menu_option == 1 or menu_option == 2 or menu_option == 3:
        return menu_option
    else:
        report_error('Invalid Option')
        start()

def ascii_to_binary(Letter, Binary):
    phrase = input_phrase()

    count = 0
    for character in phrase:
        if character in Letter:
            print(Binary[count], end = ' ')
        count += 1
            
start()
