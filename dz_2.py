def personal_sum(*numbers):
    res = 0
    incorrect_data = 0
    for nums in numbers:
        for i in nums:
            try:
                res += i
            except TypeError:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return res, incorrect_data

def calculate_average(*numbers):
    try:
        sum = personal_sum(*numbers)
        return sum[0] / (len(*numbers) - sum[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать