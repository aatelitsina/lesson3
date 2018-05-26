# Выполнить основные арифметические действия с числами: сложение, вычитание, умножение и деление. Если боту сказать “2-3=”, он должен ответить “-1”. Все выражения для калькулятора должны заканчиваться знаком равно.
# Дополнительно: не забудьте обработать возможные ошибки во вводе: пробелы, отсутствие чисел, деление на ноль.
# обработка вещественных чисел

import re
def calculate(equation):
    try:
        # equation = '21+c='.replace('=','')
        pattern = '|'.join(map(re.escape, ['+', '-', '*', '/']))
        numbers = re.split(pattern,equation)
        sign = re.findall(pattern,equation)
        for numb in range(len(numbers)):
            result = float(numbers[numb])
            numb += 1
            if '+' in sign:
                result += float(numbers[numb])
                break
            elif '-' in sign:
                result -= float(numbers[numb])
                break
            elif '/' in sign:
                result = result / float(numbers[numb])
                break
            elif '*' in sign:
                result *= float(numbers[numb])
                break
    except ZeroDivisionError:
        return 'Деление на 0!!!'
    except (SyntaxError,ValueError):
        return 'Введите числа'
    else:
        return result
        # print(sign)

# print(calculate('4.5+4.0'))
