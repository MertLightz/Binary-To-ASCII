import time

def blank_page():
    for i in range(0,100):
        print()
    return

def report_error(message):
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
    report_error('invalid choice')
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
