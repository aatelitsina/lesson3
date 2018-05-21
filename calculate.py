import re
try:
    equation = '21+c='.replace('=','')
    numbers = re.split(r'[+-/\*]',equation)
    sign = re.findall(r'[\+-/\*]',equation)
    for numb in range(len(numbers)):
        result = int(numbers[numb])
        numb += 1
        if '+' in sign:
            result += int(numbers[numb])
            break
        elif '-' in sign:
            result -= int(numbers[numb])
            break
        elif '/' in sign:
            result = result / int(numbers[numb])
            break
        elif '*' in sign:
            result *= int(numbers[numb])
            break
except ZeroDivisionError:
    print('Деление на 0!!!')
except (SyntaxError,ValueError):
    print('Введите числа')
else:
    print(result)
    # print(sign)