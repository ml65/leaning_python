# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return False
    else:
        return True

for item in numbers:
    if item > 1:
        if is_prime(item):
            primes.append(item)
        else:
            not_primes.append(item)

print ("Primes:", primes)
print ("Not Primes:", not_primes)