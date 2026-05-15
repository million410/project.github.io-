import random
from traceback import print_tb
import time

operation = ['+', '-', '*', '/']
min_operand = 3
max_operand = 12
total_problem = 10

def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operation)

    expr = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input('Press enter to start!')
print('--------------------------------')

start_time = time.time()

for i in range(total_problem):
    expr, answer = generate_problem()
    while True:
        guess = input('Problem #' + str(i+1) + ': ' + expr + ' = ')
        if guess == str(answer):
            break
        wrong += 1
end_time = time.time()
total_time = end_time - start_time

print('--------------------------------')
print('Total time: ' + str(total_time) + ' seconds')