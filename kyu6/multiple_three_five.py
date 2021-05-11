suma = 0

def multiple(n):
    global suma
    if n < 3:
        return suma
    n -= 1
    suma += n if n % 3 == 0 or n % 5 == 0 else 0
    return multiple(n)


print(multiple(10))
