#Rekenmachine
product = input(str('what should i compute: '))
list_1 = product.split(' ')
number1 = int(list_1[0])
number2 = int(list_1[2])
if list_1[1] == 'x':
    solution = number1 * number2
elif list_1[1] == '+':
    solution = number1 + number2
elif list_1[1] == '-':
    solution = number1 - number2
elif list_1[1] == '/':
    solution = float(number1/number2)
elif list_1[1] == '^':
    solution = number1 ** number2
else: 
    print('Please give other input')

print(f'the solution is {solution}')

