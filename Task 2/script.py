''' Задача: В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
'''

def NumbersToBigger(numbers):
    list = []
    count = 0

    for i in range(len(numbers)):
        
        if numbers[i] != ' ':
            if list == []:
                list.insert(0, int(numbers[i]) - 1)
                list.append(int(numbers[i]))
            else:
                list.append(int(numbers[i]))
            count = 0

        if count > 1:
            list.append(list[-1] + 1)
            if count > 2:
                del list[-1]
        
        count += 1
    return list


'''def NumbersToLess(numbers):
    list = []
    count = 0

    for i in range(len(numbers)):
        
        if numbers[i] != ' ':
            if list == []:
                list.insert(0, int(numbers[i]) + 1)
                list.append(int(numbers[i]))
            else:
                list.append(int(numbers[i]))
            count = 0

        if count > 1:
            list.append(list[-1] - 1)
            if count > 2:
                del list[-1]
        
        count += 1
    return list


print(*NumbersToBigger(data))
print(*NumbersToLess(data))
'''

path = 'Task 2\Data.txt'
data = open(path, 'r')
for line in data:
    print(*NumbersToBigger(data))
data.close()
exit()

#PS: Не успеваю доделать. 