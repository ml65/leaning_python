# Домашнее задание по теме "Форматирование строк".

#
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
team1_name = "Мастера кода"
team2_name = "Волшебники данных"
team1_time = 18015.2
team2_time = 13000.2

print("В команде %s участников: %s!" % (team1_name, team1_num))
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

print("Команда {team2} решила задач: {score2}!".format( score2 = score_2, team2=team2_name))
print(" {team1} решили задачи за {time1} с !".format(time1=team1_time, team1=team1_name))

print(f"Команды решили {score_1} и {score_2} задач.")

pri = True
if (score_1 == score_2):
    challenge_result = 'Ниьчя!'
    pri = False
elif (score_1 > score_2):
    challenge_result = "победа команды " + team1_name;
else:
    challenge_result = "победа команды " + team2_name;

print(f"Результат битвы: {challenge_result}!")
