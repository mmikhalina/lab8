import numpy as np
while True:
    print("лінійний пошук:\n")
    A = np.random.randint(0, 15, 24)
    print("mass:")
    print(A)
    i = 0
    count = 0
    while i < 24 and A[i] != 15:
        i += 1
        count += 1
    if i == 24:
        print('number', 15, 'not found')
        print('Compares:', count)
    else:
        count += 1
        print('number', 15, 'found', i)
        print('Compares:', count)

    A = np.random.randint(0, 8, 24)
    A[-1] = 3
    print("random number array :")
    print(A)
    i = 0
    count = 0
    while i < 24 and A[i] != 3:
        i += 1
        count += 1
    if i == 24:
        print('number', 3, 'not found.')
        print('Compares:', count)
    else:
        count += 1
        print('Item', 3, 'first found in position', i)
        print('Compares:', count)

    print("\nбінарний пошук:\n")
    a = np.random.randint(0, 20, 24)
    A[-1] = 15
    a.sort()
    print("mass:")
    print(a)
    i = 0
    L = 0
    R = 23
    K = 0
    flag = True

    while L <= R and flag:
        i += 1
        K = (L + R) // 2
        if a[K] == 15:
            print('number', 15, 'found', K)
            print('compares:', i)
            flag = False
        elif a[K] < 15:
            L = K + 1
        elif a[K] > 15:
            R = K - 1
    if flag:
        print('number', 15, 'not found.')
        print('compares:', i)
    print()

    a = np.random.randint(0, 10, 24)
    a.sort()
    print("mass:")
    print(a)
    i = 0
    L = 0
    R = 23
    K = 0
    flag = True

    while L <= R and flag:
        i += 1
        K = (L + R) // 2
        if a[K] == 15:
            print('number', 15, 'founded', K)
            print('compares:', i)
            flag = False
        elif a[K] < 15:
            L = K + 1
        elif a[K] > 11:
            R = K - 1
    if flag:
        print('number', 15, 'not found.')
        print('compares:', i)

    print("\nпрямий пошук підрядка:\n")
    text = "my name is Johan, your name"
    pattern = "your"
    i = -1
    j = 0
    count = 0
    print('text:', text)
    print('pattern:', pattern)
    while (j < len(pattern)) and i < (len(text) - len(pattern)):
        j = 0
        i += 1
        while j < len(pattern) and pattern[j] == text[i + j]:
            j += 1
            count += 1
    if j == len(pattern):
        print('pattern found in symbol', i)
    else:
        print('not found.')
    print('compares', count)
    print()
    text = "my name is Johan, your name"
    pattern = "I'm Kendrick"
    i = -1
    j = 0
    count = 0
    print('text:', text)
    print('pattern:', pattern)
    while (j < len(pattern)) and i < (len(text) - len(pattern)):
        j = 0
        i += 1
        while j < len(pattern) and pattern[j] == text[i + j]:
            j += 1
            count += 1
    if j == len(pattern):
        print('not found', i)
    else:
        print('not found.')
    print('compares', count)

    if input('Enter to reload') == '':
        continue
    break