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
    print('{:^50}'.format('1 - ASCII TO BINARY'))
    time.sleep(0.1)
    print('{:^50}'.format('2 - BINARY TO ASCII'))
    time.sleep(0.1)
    print('{:^50}'.format('3 - QUIT           '))
    time.sleep(0.1)
    return

def start():
    space = [' ','00100000']
    uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']    
    upper_binary = ['01000001','01000010','01000011','01000100','01000101','01000110','01000111','01001000','01001001','01001010','01001011','01001100','01001101','01001110','01001111','01010000','01010001','01010010','01010011','01010100','01010101','01010110','01010111','01011000','01011001','01011010']
    lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    lower_binary = ['01100001','01100010','01100011','01100100','01100101','01100110','01100111','01101000','01101001','01101010','01101011','01101100','01101101','01101110','01101111','01110000','01110001','01110010','01110011','01110100','01110101','01110110','01110111','01111000','01111001','01111010',]
    
    program_end = False
    while not program_end:
        display_menu()
        menu_option = get_menu_option()
        if menu_option == 1:
            ascii_to_binary(space, uppercase, upper_binary, lowercase, lower_binary)
        elif menu_option == 2:
            binary_to_ascii(space, uppercase, upper_binary, lowercase, lower_binary)
        elif menu_option == 3:
            program_end = True
        else:
            report_error('INVALID OPTION')

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
        binary = input('BINARY: ')

        if binary == '':
            report_error('BINARY CANNOT BE BLANK')
        else:
            check = True
            return binary

def phrase_input():
    check = False
    while check == False:
        blank_page()
        print('{:^50}'.format('- ENTER PHRASE TO CONVERT TO BINARY -'))
        time.sleep(0.1)
        print()
        time.sleep(0.1)
        phrase = input('ASCII: ')

        if phrase == '':
            report_error('PHRASE CANNOT BE BLANK')
        else:
            check = True
            return phrase

def get_menu_option():
    print()
    time.sleep(0.1)
    check = False
    while check == False:
        try:
            menu_option = int(input('ENTER: '))
            check = True
        except:
            report_error('INVALID DATA TYPE')
            display_menu()
            
    if menu_option == 1 or menu_option == 2 or menu_option == 3:
        return menu_option
    else:
        report_error('INVALID OPTION')
        start()

def output_converted(converted):        
    if converted == '':
        report_error('INVALID INPUT')
        return
    else:
        print('- {:^50}-'.format(converted))
        print()
        print('{:^50}'.format('- PRESS ENTER TO CONTINUE -'))
        input()
        return

def ascii_to_binary(space, uppercase, upper_binary, lowercase, lower_binary):
    phrase = phrase_input()
    print()
    time.sleep(0.1)
    count = 0
    converted = ''
    
    for x in range(0, len(phrase)):
        for i in range(0, len(uppercase)): 
            if phrase[x] == uppercase[i]:
                converted += upper_binary[i] + ' '
                
            elif phrase[x] == lowercase[i]: 
                converted += lower_binary[i] + ' '
                
            elif phrase[x] == space[0]: 
                converted += space[1] + ' '
                break

    output_converted(converted)

def binary_to_ascii(space, uppercase, upper_binary, lowercase, lower_binary):
    input_binary = binary_input()
    print()
    time.sleep(0.1)
    count = 0
    converted = ''
    edited_binary = input_binary.split(' ')

    for x in range(0, len(edited_binary)):
        for i in range(0, len(upper_binary)):
            if edited_binary[x] == upper_binary[i]:
                converted += uppercase[i]
                
            elif edited_binary[x] == lower_binary[i]:
                converted += lowercase[i]
                
            elif edited_binary[x] == space[1]:
                converted += space[0]
                break

    output_converted(converted)

blank_page()
report_error('WELCOME')
start()
