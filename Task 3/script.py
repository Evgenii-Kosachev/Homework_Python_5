''' Задача: Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
    Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
'''

def SearchUniqueElements(numbers):
    res = [i for i in numbers if numbers.count(i) == 1]
    return res

data = [1, 2, 3, 5, 1, 5, 3, 10]

print(SearchUniqueElements(data))