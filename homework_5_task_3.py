# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.Выполнить подсчет средней величины дохода сотрудников.


with open("The_firm.txt", "r", encoding='utf-8') as f:
    staff = 0
    for line in f:
        staff += 1
    print("Количество сотрудников: ", staff)
with open('The_firm.txt', 'r', encoding='utf-8') as f:
    staff = {}
    for line in f:
        key, value = line.split()
        staff[key] = value
        if int(value) <= 20000:
            print(f'{key}: зарплата меньше 20000')
with open('The_firm.txt', 'r', encoding='utf-8') as f:
    sum = 0
    count = 0
    for line in f:
        count += 1
        sum += float(line.split()[1])
    salary = sum / count

    print ('средняя зароботная плата составляет: ', salary)
 # не могу понять как посчитать среднюю зп

