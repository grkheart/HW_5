# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("task_2.txt") as f:
    line_count = 0
    for line in f:
        line_count += 1
print("Количество строк", line_count)
for line in open("task_2.txt").readlines():
    print(len(line))