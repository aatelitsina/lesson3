import re
def calculate(equation):
    try:
        # equation = '21+c='.replace('=','')
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
        return 'Деление на 0!!!'
    except (SyntaxError,ValueError):
        return 'Введите числа'
    else:
        return result
        # print(sign)

# print(calculate('4+4'))