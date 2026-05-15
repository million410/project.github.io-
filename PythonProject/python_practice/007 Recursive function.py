#Recursive Function(function that can call itself)

# example with loop-------
def countdown(n):
    while True:
        if n < 0:
            break
        print(n)
        n -= 1
countdown(4)

# RECURSIVE COUNTDOWN--------
def countdown(n):
    #base case
    if n < 0:
        return n
    # Recursive case
    print(n)
    countdown(n-1)
print('Recursive Function')
countdown(4)
# factorial
def factorial(n):
    print('Enter the factorial of {}'.format(n))
    if n == 0:
        print(f'Base case reaches: Returning 1')
        return 1
    result = n * factorial(n-1)
    print(f'Returning {result} for factorial of {n}')
    return result
print(factorial(5))
#-----Ex-----------------
def sum_digits(number):
    # Base case(return single digit)
    if number < 10:
        return number
    #Recursive case(Calculate digits sum)
    digits = []
    for str_num in digits:
        num = int(str_num)
        digits.append(num)
    total = sum(digits)
    return sum_digits(total)
# Compare Results
print(sum_digits(38))

def fact(n):
    if n == 0:
        return 1
    prod = n
    prod *= fact(n - 1)
    return prod
print(fact(5))
