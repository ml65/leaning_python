# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for item in numbers:
    is_prime = True
    for i in range(2,item):
        if item % i == 0:
            is_prime = False
    if is_prime:
        primes.append(item)
    else:
        not_primes.append(item)

print ("Primes:", primes)
print ("Not Primes:", not_primes)