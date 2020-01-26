import time

def blank_page():
    for i in range(0,100):
        print()
    return

def report_error(message):
    blank_page()
    print('-{:^50}-'.format(message))
    time.sleep(1)
    blank_page()
    return

def display_menu():
    blank_page()
    print('{:^50}'.format('1 - ASCII to Binary'))
    time.sleep(0.1)
    print('{:^50}'.format('2 - Binary to ASCII'))
    time.sleep(0.1)
    print('{:^50}'.format('3 - Quit           '))
    time.sleep(0.1)
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
            report_error('Invalid Option')

def binary_input():
    check = False
    while check == False:
        blank_page()
        print('{:^50}'.format('- ENTER BINARY TO CONVERT TO ASCII -'))
        time.sleep(0.1)
        print('{:^50}'.format('- INCLUDE SPACES BETWEEN EACH 8BIT -'))
        time.sleep(0.1)
        print()
        time.sleep(0.1)
        binary = input('Binary: ')

        if binary == '':
            report_error('Binary Cannot Be Blank')
        else:
            check = True
            return binary

def phrase_input():
    check = False
    while check == False:
        blank_page()
        print('{:^50}'.format('- ENTER PHRASE TO CONVERT TO BINARY -'))
        time.sleep(0.1)
        print('{:^50}'.format('- MUST BE UPPER CASE -'))
        time.sleep(0.1)
        print()
        time.sleep(0.1)
        phrase = input('ASCII: ')

        if phrase == '':
            report_error('Phrase Cannot Be Blank')
        else:
            check = True
            return phrase

def get_menu_option():
    print()
    time.sleep(0.1)
    check = False
    while check == False:
        try:
            menu_option = int(input('Enter a number: '))
            check = True
        except:
            report_error('Invalid Data Type')
            display_menu()
            
    if menu_option == 1 or menu_option == 2 or menu_option == 3:
        return menu_option
    else:
        report_error('Invalid Option')
        start()

def output_converted(converted):        
    if converted == '':
        report_error('Invalid Input')
        return
    else:
        print('- {:^50}-'.format(converted))
        print()
        print('{:^50}'.format('- PRESS ENTER TO CONTINUE -'))
        input()
        return

def ascii_to_binary(Letter, Binary):
    phrase = phrase_input()
    print()
    time.sleep(0.1)
    count = 0
    converted = ''
    
    for x in range(0, len(phrase)):
        for i in range(0, len(Letter)):
            if phrase[x] == Letter[i]:
                converted += Binary[i] + ' '

    output_converted(converted)

def binary_to_ascii(Letter, Binary):
    input_binary = binary_input()
    print()
    time.sleep(0.1)
    count = 0
    converted = ''
    edited_binary = input_binary.split(' ')

    for x in range(0, len(edited_binary)):
        for i in range(0, len(Binary)):
            if edited_binary[x] == Binary[i]:
                converted += Letter[i]

    output_converted(converted)
    
start()
