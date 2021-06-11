# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summ():
    try:
        with open('filesumm.txt', 'w+') as f:
            line = input('Введите цифры через пробел \n')
            f.writelines(line)
            num = line.split()
            print(sum(map(int, num)))
    except ValueError:
        print('Неправильнное число')


summ()
