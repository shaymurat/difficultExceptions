def personal_sum(numbers):
    '''
    Возвращает кортеж из суммы коллекции numbers и количества
    объектов коллекции, не являющихся числами.
    '''
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
    return (result, incorrect_data)


def calculate_average(numbers):
    '''
    Возвращает среднее арифметическое коллекции numbers.
    Если numbers - не коллекция, возвращает None.
    '''
    try:
        length = len(numbers)
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    total, rejected = personal_sum(numbers)
    good = length - rejected
    try:
        avg = total / good
    except ZeroDivisionError:
        return 0
    return avg


if __name__ == '__main__':
    # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 1: {calculate_average("1, 2, 3")}')

    # Учитываются только 1 и 3
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')

    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция

    # Всё должно работать
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
