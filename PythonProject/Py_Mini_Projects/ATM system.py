'ATM system'
personal_bank_info = {
    'Name': 'Million',
    'Country': 'Ethiopia',
    'Bank_Account': 10000329810,
    'Balance': 2000,
    'Date': 12/1/2026,
    'MRA PIN': 111001,
    'Account PIN': 120032,
}
mini_statement = {}
def atm_system():
    while True:
        print('---ATM MENU---')
        print('1.Check balance')
        print('2.Withdraw money')
        print('3.Deposit')
        print('4.Change PIN')
        print('5.Mini statement')
        print('6.Update personal info')
        print('7.Exit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            count_d = 0
            PIN_n = int(input('Please insert PIN: '))
            if PIN_n == personal_bank_info['Account PIN']:
                count_d += 1
                personal_bank_info['Date'] = 13 + count_d/1/2026
                mini_statement.update({'Date': 13 + count_d/1/2026,})
                print('Your current balance is: ' + str(personal_bank_info['Balance']))
                print('To continue, press 1 else press other key')
                choice_1 = int(input('Enter your choice: '))
                if choice_1 == 1:
                    atm_system()
                else:
                    print('Good bye!')
                    break
            if PIN_n != personal_bank_info['Account PIN']:
                print('Wrong PIN!, try again')
                print('1.Continue')
                print('2.Exit')
                choice_2 = int(input('Enter your choice: '))
                if choice_2 == 1:
                    continue
                elif choice_2 == 2:
                    print('Have a nice time!, Existed')
                    break
                else:
                    print('Invalid choice!')
        elif choice == 2:
            PIN_n = int(input('Please insert PIN: '))
            if PIN_n == personal_bank_info['Account PIN']:
                amount_n = int(input('Please insert amount: '))
                personal_bank_info['Balance'] = personal_bank_info['Balance'] - amount_n
                print('Your current balance is: ' + str(personal_bank_info['Balance']))
                print('Take the cash!')
            else:
                print('Wrong PIN!, try again')
                print('press 0 to continue')
                choice_3 = int(input('Enter your choice: '))
                if choice_3 == 0:
                    atm_system()
                else:
                    print('Good bye!')
                    break
        elif choice == 3:
            PIN_n = int(input('Please insert MRA PIN: '))
            if PIN_n == personal_bank_info['MRA PIN']:
                amount_n = int(input('Please insert amount: '))
                personal_bank_info['Balance'] = personal_bank_info['Balance'] + amount_n
                print('Your current balance is: ' + str(personal_bank_info['Balance']))
                print('To continue, press 1 else press other key')
                choice_4 = int(input('Enter your choice: '))
                if choice_4 == 1:
                    atm_system()
                else:
                    print('Wrong PIN!, try again')
                    break
            else:
                print('Wrong PIN!, please check it again!')
                break
        elif choice == 4:
            choice_5 = int(input('Enter your Previous PIN: '))
            if choice_5 == personal_bank_info['Account PIN']:
                personal_bank_info['Account PIN'] = int(input('Please insert New PIN: '))
                choice_6 = int(input('Enter 1 to continue: '))
                if choice_6 == 1:
                    continue
                else:
                    print('Good bye!')
                    break
            else:
                print('Wrong PIN!, please check it again!')
        # choice 5 written here
        elif choice == 6:
            PIN_n = int(input('Please insert PIN: '))
            if PIN_n == personal_bank_info['Account PIN']:
                print('1.Name')
                print('2.Account Number')
                print('3.Country')
                Changed_info = int(input('Enter your choice: '))
                if Changed_info == 1:
                    check = input(f'Are you sure to change your name ({personal_bank_info['Name']}): ').lower()
                    if check == 'yes':
                        personal_bank_info['Name'] = input('Please insert your New name: ')
                        print('you successfully changed your name!')
                    else:
                        continue
                elif Changed_info == 2:
                    check = input(f'Are you sure to change your Account number ({personal_bank_info['Bank_Account']}): ').lower()
                    if check == 'yes':
                        personal_bank_info['Bank_Account'] = int(input('Please insert your New Bank_Account: '))
                        print('you successfully changed your Bank_Account!')
                    else:
                        continue
                elif Changed_info == 3:
                    check = input(f'Are you sure to change your Country ({personal_bank_info['Country']}): ').lower()
                    if check == 'yes':
                        personal_bank_info['Country'] = input('Please insert your New Country: ')
                        print('you successfully changed your Country!')
                    else:
                        continue
        elif choice == 7:
            print('Have a nice time!, Existed')
            break
atm_system()
