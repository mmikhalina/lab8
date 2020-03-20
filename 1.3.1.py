import numpy as np

print("press 1 for reverse\npress 2 for transp\npress 3 for multiply\npress 4 for exchange all elements 0\n")
while True:
    try:
        num = int(input("your number = "))
        # read the number of the completed program
    except ValueError:
        print('only digit 1, 2, 3 or 4')
        # we check for an error (nothing can be entered except digits)
    if (num == 1):
        print("your martrix is linear !")
        lenght = int(input())
        matrix = np.zeros((lenght, 1), dtype=int)
        # allocate space for the array
        new_matrix = np.zeros((lenght, 1), dtype=int)
        # allocate space for the array
        i = 0
        for i in range(lenght):
            matrix[i, 0] = int(input())
            # the user fills in the data
        count = lenght - 1
        #in order to go from the end, I create a variable to pass the final parameter in the array (minus one because the last element is not inclusive)
        for i in range(lenght):
            new_matrix[i, 0] = matrix[count, 0]
            # I fill the new array with data from the initial but from the final valueия
            count -= 1
            # so that the array is filled with new data, you need to go to the initial (from the end)
        print("first version")
        print(matrix)
        print("reverse result")
        print(new_matrix)


    elif (num == 2):
        print('default size of your matrix 3x3')
        matrix = np.zeros((3, 3), dtype=int)
        # allocate space for the array
        new_matrix = np.zeros((3, 3), dtype=int)
        # allocate space for the array
        i, j = 0, 0
        for i in range(3):
            for j in range(3):
                matrix[i, j] = int(input())
                # the user fills in the data
        for i in range(3):
            for j in range(3):
                new_matrix[i, j] = matrix[j, i]
                # assign the columns of the initial array to the lines of the created and vice versa (transposed matrix)
        print(f'matrix before\n{matrix}')
        print(f'matrix after\n{new_matrix}')


    elif (num == 3):
        print('default size both of your matrix 3x3')
        A = np.zeros((3, 3), dtype=int)
        # allocate space for the arrayа
        B = np.zeros((3, 3), dtype=int)
        # allocate space for the array
        C = np.zeros((3, 3), dtype=int)
        # allocate space for the array
        i, j = 0, 0
        for i in range(3):
            for j in range(3):
                A[i, j] = int(input())
        # the user fills in the data
        i, j = 0, 0
        for i in range(3):
            for j in range(3):
                B[i, j] = int(input())
        # the user fills in the data
        i, j = 0, 0
        for i in range(3):
            for j in range(3):
                C[i, j] = A[i, 0] * B[0, j] + A[i, 1] * B[1, j] + A[i, 2] * B[2, j]
            # matrix multiplication formula
        print("first matrix")
        print(A)
        print("second mtrix")
        print(B)
        print("result matrix")
        print(C)


    elif (num == 4):
        print('default size both of your matrix 4x4')
        matrix = np.zeros((4, 4), dtype=int)
        i, j = 0, 0
        for i in range(4):
            for j in range(4):
                matrix[i, j] = int(input())
                if (matrix[i, j] < 0):
                    matrix[i, j] = 0
                    # checking the condition, if the element is less than 0, replace it with 0
        print(matrix)
    else:
        continue
    if input('Enter') == '':
        continue
    break