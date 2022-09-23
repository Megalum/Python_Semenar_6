# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

f = list(map(int, '1 2 3 5 1 5 3 10 22 35 48 2 48'.split()))
res = [1, 2, 3, 5, 1, 5, 3, 10, 22, 35, 48, 2, 48]
output = []
while f:
    flag = True
    i = 1
    while i != len(f):
        if f[0] == f[i]:
            flag = False
            f.pop(i)
            i -= 1
        i += 1
    if flag:
        output.append(f[0])
    f.pop(0)
print(f'{res} => {output}')