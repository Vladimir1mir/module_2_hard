from random import randint

def rebus (n):
    if n < 3 or n > 20:
        return
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                result = result + f'{i}' + f'{j}'

    return str(n) + ' - ' + str(result)

count = randint(3,20)
rebus(count)
print(rebus(count))
