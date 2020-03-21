import numpy as np

while True:
    try:
        size = int(input("size of your matrix = "))
    except ValueError:
        print("only digits")

    matrix1 = np.zeros((size, size), dtype=int)
    # creating an array
    matrix2 = np.zeros((size, size), dtype=int)
    # creating an array
    mult_matrix = np.zeros((size, size), dtype=int)


    for i in range(size):
        for j in range(size):
            matrix1[i, j] = int(input())
            # first array data

    for i in range(size):
        for j in range(size):
            matrix2[i, j] = int(input())
            # second array data
    i=0
    j=0
    count=0
    sum=0
    for i in range(size):
        for j in range(size):
            for count in range(size):
                sum += matrix1[i][count] * matrix2[count][j]
                # создам переменную которая будет обсчитывать для каждого элемента его значение
            matrix_mult[i][j] = sum
            # записываем в наш элемент массива его значение
            sum = 0
            # обнуляем что бы обсчет следующего элемента начался с 0
    print(matrix_mult)

    if input('Enter') == '':
        continue
    break