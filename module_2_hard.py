# Дополнительное практическое задание по модулю*
# Дополнительное практическое задание по модулю: "Основные операторы"

def indiana_password(num):
    result = '';
    for i in range(1,21):
        for j in range(1,21):
            if i < j:
                if 0 == num % (i + j):
                    result  += str(i) + str(j)
    return result

while 1 > 0:
    number = int(input("Введите число: "))
    print ("Пароль:", indiana_password(number))