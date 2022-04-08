n_bilet = int(input('Здравствуйте! Введите количество билетов, которое Вы хотите приобрести: '))
age = [int(input('Введите возраст участника: ')) for i in range(n_bilet)]
summa = 0
for i in range(n_bilet):
    if 18<=age[i]<25:
        summa+=990
    elif 25<=age[i]:
        summa+=1390
if n_bilet <= 3:
    print('Сумма заказа составляет ',summa,' руб.')
else:
    print('Сумма заказа с учетом 10% скидки составляет',summa-summa*0.1,'руб.')
