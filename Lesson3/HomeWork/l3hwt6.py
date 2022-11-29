# 6 - Бухгалтер Люба заполняет ведомость по зарплате. У Любы есть два файла - один с фио,
# другой - с зарплатой за декабрь.
# Ей нужно создать третий файл вида "фио, зарплата".
# Но Люба совершила ошибку.
# Она забыла, что в декабре все работники должны получить зарплату по повышенному коэффициенту: 1.5
# А еще у босса есть список любимчиков, которым повышенный коэффициэнт будет 2,
# их фио нужно выделить высоким регистром: они получат зарплату раньше.
# Создайте сначала словарь на основе первых двух файлов, а дальнейшие действия - с созданным словарем.
# Пример:
# Файл 1: (разумеется, у вас больше)
# Гарри Джеймс Поттер
# Дадли Вернон Дурсль
# Файл 2:
# 10000
# 12000
# Финальный файл:
# Гарри Джеймс Поттер, 15000
# ДАДЛИ ВЕРНОН ДУРСЛЬ 24000

def employers_data():
    names = [input('Type name of employer:\n') for i in range(2)]
    return names


def wage_data():
    wages = [int(input("Type wages for employers:\n")) for i in range(2)]
    return wages


def favorits_list():
    favors = []
    switch = True
    while switch:
        favors.append(input("Type name for bosses favourites or type 'exit' to end list:\n"))
        if favors[-1] == 'exit':
            switch = False
            favors.pop(-1)
    return favors


def wage_common(emp, wgs):
    wages = {emp[i]: wgs[i] for i in range(len(emp))}
    return wages


def wage_result(wgs_data, favs, coef_emp, coef_favs):
    for i in wgs_data.keys():
        if i in favs:
            wgs_data[i] = int(wgs_data[i] * coef_favs)
        else:
            wgs_data[i] = int(wgs_data[i] * coef_emp)
    for i in favs:
        wgs_data[i.upper()] = wgs_data.pop(i)
    return wgs_data

def print_wages_list(dct, entry_string):
    print(f'{entry_string}')
    for i in dct.keys():
        print(f'{i}: {dct[i]}')

data_wage = wage_common(emp=employers_data(), wgs=wage_data())
print_wages_list(data_wage, 'Standart wages list')
result_wage = wage_result(data_wage, favorits_list(), 1.5, 2)
print_wages_list(result_wage, 'Final wages list 12.2022')
