# (необязательное) Напишите программу, которая принимает на стандартный вход список игр футбольных команд 
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:

# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# Вывод программы необходимо оформить следующим образом:

# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# Порядок вывода команд произвольный.

# Sample Input:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:

# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

count = int(input('Sample Input: '))
input_list = []
cort_list = [(0, 2)]
for i in range(count):
    input_list.append(list(input().split(';')))

output_set = []
for i in range(count):
    for j in cort_list[0]:
        output_set.append(f"{input_list[i][j]}")
output_set = set(output_set)
output_name = []
for i in output_set:
    output_name.append(i)

output_game = []
for k in output_name:
    col = 0
    for i in range(count):
        for j in cort_list[0]:
            if k == input_list[i][j]:
                col += 1
    output_game.append(col)

output_win = [[0,0,0,0] for i in range(len(output_game))]
for i in range(count):
    if int(input_list[i][1]) < int(input_list[i][3]):
        for j in range(len(output_name)):
            if output_name[j] == input_list[i][2]:
                output_win[j][3] += 3
                output_win[j][0] += 1
                break
        for j in range(len(output_name)):
            if output_name[j] == input_list[i][0]:
                output_win[j][2] += 1
                break
    elif int(input_list[i][1]) == int(input_list[i][3]):
        for j in range(len(output_name)):
            if output_name[j] == input_list[i][0]:
                output_win[j][3] += 1
                output_win[j][1] += 1
                break
        for j in range(len(output_name)):
            if output_name[j] == input_list[i][2]:
                output_win[j][3] += 1
                output_win[j][1] += 1
                break
    if int(input_list[i][1]) > int(input_list[i][3]):
        for j in range(len(output_name)):
            if output_name[j] == input_list[i][0]:
                output_win[j][3] += 3
                output_win[j][0] += 1
                break
        for j in range(len(output_name)):
            if output_name[j] == input_list[i][2]:
                output_win[j][2] += 1
                break

output = []
for i in range(count):
    line = []
    line.append(output_name[i])
    line.append(output_game[i])
    for j in output_win[i]:
        line.append(j)
    output.append(line)
for i in range(count):
    output_string = output[i][0] + ': '
    for j in range(1, len(output[i])):
        output_string += str(output[i][j]) + ' '
    print(output_string)