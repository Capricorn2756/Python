import os
os.chdir('/Users/goldk_000/Documents/Python/Cu')
with open('textbuff.xyz', 'w') as MyBuffFile:
    a = 3.62    #постоянная решётки
    X = [0.0, 0.0, 0.0, 0.0, a, a, a, a, 0.0, a/2, a/2, a/2, a, a/2]
    Y = [0.0, 0.0, a, a, 0.0, 0.0, a, a, a/2, 0.0, a/2, a/2, a/2, a]    #массив координат для элементарной ячейки
    Z = [0.0, a, 0.0, a, 0.0, a, 0.0, a, a/2, a/2, 0.0, a, a/2, a/2]
    nX = 2
    nY = 2    #размер решётки 
    nZ = 2
    i = 1
    j = 0
    length = len(X)
    while i < nX:   #трансляция по X
        while j < length:
            X.append(X[j] + a * i)
            Y.append(Y[j])
            Z.append(Z[j])
            j += 1
        i += 1
    i = 1
    j = 0
    length = len(Y)
    while i < nY:   #трансляция по Y
        while j < length:
            X.append(X[j])
            Y.append(Y[j] + a * i)
            Z.append(Z[j])
            j += 1
        i += 1
    i = 1
    j = 0
    length = len(Z)
    while i < nZ:   #трансляция по Z
        while j < length:
            X.append(X[j])
            Y.append(Y[j])
            Z.append(Z[j] + a * i)
            j += 1
        i += 1
    i = 0
    while i < len(Z):
        MyBuffFile.write('Cu ')
        MyBuffFile.write(str(X[i]) + ' ')
        MyBuffFile.write(str(Y[i]) + ' ')
        MyBuffFile.write(str(Z[i]) + '\n')
        i += 1
    MyBuffFile.close()
    lines_seen = set() #массив точек без повторов
    MyResult = open('MyResult.xyz', 'w')
    MyBuffFile = open('textbuff.xyz', 'r')
    MyResult.write('\n    \n')
    for line in MyBuffFile:
        if line not in lines_seen: #если новая точка
            MyResult.write(line)
            lines_seen.add(line)
    MyResult.seek(0,0)
    MyResult.write(str(len(lines_seen)) + '\n' )  #добавление числа точек в начало файла
    MyResult.close()
    MyBuffFile.close()
