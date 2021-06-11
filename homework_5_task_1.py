# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

fileinput = input('file_task: ')
f = open(fileinput, 'w', encoding="utf-8")
while True:
    a = input()
    if a == '': break
    f.write(a + '\n')
f.close()
