from http.cookiejar import uppercase_escaped_char

random_words = [
    'Lighthouse', 'Cat', 'Umbrella', 'Giraffe',
    'Success', 'Volcano', 'Balloon'
    'Butterfly', 'Mississippi', 'Strawberry'
]

#--FINDING MOST FREQUENT LETTER---------

#----------------------
'one'
# def most_frequent_words(word):
#     print('-' * 50)
#     print(f'🔎 Checking word: {word}')
#     word = word.lower()
#     # Count letter---------
#     dict_count = {}
#     for letter in word:
#         if letter not in dict_count:
#             count = word.count(letter)
#             dict_count[letter] = count
#     # print report----
#     for k, v in dict_count.items():
#         if count > 1:
#             print(f'{k} used {v} times')
#         else:
#             print(f'{k} used {v} time')
#     # find max count------
#     max_count = max(dict_count.values())
#     max_letter = []
#     for k, v in dict_count.items():
#         if v == max_count:
#             max_letter.append(k)
#     # report result-----------
#     print(f'The most frequent letter is {max_letter}. Used {max_count } times')
# # 🌟 Main
#
# for word in random_words:
#     most_frequent_words(word)

#--Ex.Create password checker-------------

# Is Your Password Secure 🔐?
print('✅ Creating a New Account')
user_name = input('Username: ')
password = input('Password: ')
print('-' * 50)


def check_pass_name():
        # checking name
            #Start with capital letter
            #At least 3 char
            #Only english letter
            #Maximum space 1
        # 📦Placeholders
        symbols      = '~!@#$%^&&*()_+/-*?><|;[]{}'
        check_length = False
        check_digit  = False
        check_symbol = False
        check_upper  = False
        check_lower  = False
        check_no_spaces = False
        # for name ---------
        start_with_capital = False
        char_length        = False
        only_letters       = False
        max_spaces         = False
        # checking name-----
        if user_name[0].isupper():
            start_with_capital = True
        if len(user_name) > 2:
            char_length = True
        if user_name.isalpha():
            only_letters = True
        if user_name.count(' ') <= 1:
            max_spaces = True
        checks_n = [start_with_capital,
                    char_length ,
                    only_letters,
                    max_spaces]

        if not all(checks_n):
            print('Please check your name!')
            if not start_with_capital:
                print('❌ Please start with capital letters!')
            if not char_length:
                print('❌ char length must be greater than 2!')
            if not only_letters:
                print('❌ Only letters are allowed!')
            if not max_spaces:
                print('❌ Only one spaces are allowed!')
        # Security Checks
        if len(password) >= 8:
            check_length = True
        if ' ' not in password:
            check_no_spaces = True
        for char in password:
            if char.isdigit():
                check_digit = True
            if char.isupper():
                check_upper = True
            if char.islower():
                check_lower = True
            if char in symbols:
                check_symbol = True
        # Display result
        checks = [check_length, check_digit, check_symbol, check_upper, check_lower, check_no_spaces]
        if all(checks)and all(checks_n):
            print('✅ Account Created Successfully')
        elif all(checks):
            print('✅ Password Created Successfully, ⚠️ but check your name if correct')
        elif all(checks_n):
            print('✅ Good naming!')
        else:
            print('Password is not enough strong!')
            if not check_symbol:
                print(f'❌ At least one symbol{symbols} is required!')

            if not check_length:
                print('❌ At least eight characters is required!')
            if not check_digit:
                print('❌ At least one digit is required!')
            if not check_upper:
                print('❌ At least one uppercase letter is required!')
            if not check_lower:
                print('❌ At least one lowercase letter is required!')
            if not check_no_spaces:
                print('❌ Should not contain spaces.')
check_pass_name()
def add(a,b,c,d,):
    sum_n = a + b + c + d
    return sum_n
print(add(345,3,89,5))
def numbers():
    yield 1
    yield 2
    yield 3
for i in numbers():
    print(i)
x = 10
def change():
    global x
    x = 20
change()
print(x)

def outer():
    y = 2
    def inner():
        nonlocal y
        y = 6
    inner()
    print(y)
outer()
def square(b):
    return b ** 2
print(square(67))

vowels = ['a', 'e', 'i', 'o', 'u']

def vowel_count(word):
    word = word.lower()
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    print(count)
vowel_count('Education')

print('python')