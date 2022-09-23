# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# Добавьте возможность использования скобок, меняющих приоритет операций.
# (1+2)*3 => 9

number_list = []
char_list = []

def math(op, x, y):
    return (op(x, y))

def calc(char, col, st, en):
    global number_list
    global char_list
    if char == '*':
        number_list[col - st + en - 1] = math(lambda x, y: x*y, float(number_list[col - st + en - 1]), float(number_list[col - st + en]))
    elif char == '/': 
        number_list[col - st + en - 1] = math(lambda x, y: x/y, float(number_list[col - st + en - 1]), float(number_list[col - st + en])) 
    elif char == '+':
        number_list[col - st + en - 1] = math(lambda x, y: x+y, float(number_list[col - st + en - 1]), float(number_list[col - st + en])) 
    elif char == '-':
        number_list[col - st + en - 1] = math(lambda x, y: x-y, float(number_list[col - st + en - 1]), float(number_list[col - st + en])) 
    number_list.pop(col - st + en)
    char_list.pop(st)           


f = '26.3-((1+2.3*2)*9)/3'
operation = ['(', ')', '*', '/', '+', '-']
count = ''
flag = True
for i in f:
    for j in operation:
        if i == j:
            char_list.append(j)
            flag = False
            break
    if flag:
        count += i
    else:
        if count != '':
            number_list.append(count)
            count = ''
        flag = True
if count != '':
    number_list.append(count)

flag = False
while char_list:
    col = 0
    nach = 0
    end = 0    
    for i in range(len(char_list)):
        if char_list[i] == '*' or char_list[i] == '/' or char_list[i] == '+' or char_list[i] == '-':
            col += 1
        if char_list[i] == '(':
            nach = i + 1
            flag = True
        elif char_list[i] == ')':
            end = i - 1
            break
    if flag:              
        for j in range(end - nach + 1):
            flag_op = True
            for i in range(nach, end + 1):
                if char_list[i] == '*':
                    calc('*', col, i, end)
                    end -= 1
                    col -= 1
                    flag_op = False
                    break
                elif char_list[i] == '/':
                    calc('/', col, i, end)
                    end -= 1
                    col -= 1
                    flag_op = False
                    break
            if flag_op:
                for i in range(nach, end + 1):
                    if char_list[i] == '+':
                        calc('+', col, i, nach)
                        end -= 1
                        col -= 1
                    elif char_list[i] == '-':
                        calc('-', col, i, nach)
                        end -= 1    
                        col -= 1            
                break
        char_list.pop(end+1)
        char_list.pop(nach-1)
        flag = False
    else:
        for j in range(len(char_list)):         
            flag_op = True
            for i in range(len(char_list)):                
                if char_list[i] == '*':
                    calc('*', i + 1, i, i)
                    flag_op = False
                    break
                elif char_list[i] == '/':
                    calc('/', i + 1, i, i)
                    flag_op = False
                    break
            if flag_op:
                while char_list:
                    i = 0
                    if char_list[i] == '+':
                        calc('+', 1, 0, 0)
                    elif char_list[i] == '-':
                        calc('-', 1, 0, 0)             
                break

print(f'{f} => {round(number_list[0], 3)}')