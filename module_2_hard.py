from random import randint

def rebus (n):
    if 3 < n < 20:
        return
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if (i + j) % n == 0:
                result = result + f'{i}' + f'{j}'
    return result

count = randint(3,20)
rebus(count)