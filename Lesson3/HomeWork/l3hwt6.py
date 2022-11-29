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

def employers_data(num):
    '''
    Generates list for employers at company

    :param num: takes amount of employers
    :return: employers list
    '''
    names = [input('Type name of employer: ') for i in range(num)]
    return names


def wage_data(emp):
    '''
    Generates list for employer's wage. List length can't be larger then employers list

    :param emp: employers list
    :return: wages list
    '''
    wages = []
    for i in range(len(emp)):
        val = ''
        while not val.isdigit():
            val = input('Type wage value: ')
            if val.isdigit() and int(val) > 0:
                wages.insert(i, int(val))
            else:
                print('Type natural number pls. They working not for food or letters')
    return wages


def favorits_list(emp):
    '''
    Gives Lyuba opportunity to choose bosses favourites from employers list

    :param emp: employers list
    :return: favourites list
    '''
    favors = []
    print('Choose bosses favourite employers')
    for i in emp:
        user_choice = input(f'Do you want to add {i}? (Y/N)\n')
        if user_choice.lower() in ('yes', 'y', 'ye', 'yep'):
            favors.append(i)
            print('Success')
        else:
            print('Seems like no...Ok!')
    return favors


def wage_common(emp, wgs):
    '''
    Generates dictionary with "employer - wage" dependance where wage is chosen by Lyuba

    :param emp: takes list of employers
    :param wgs: takes list of employer's wages
    :return: dictionary with emp values as keys, and wgs values as items
    '''
    wages = {}
    for i in range(len(emp)):
        user_choise = input(f"What wage's value is for {emp[i]}?\n" \
                            f"Choice right position from following list:\n{wgs}\n" \
                            f"Type position from 1 to {len(wgs)}:\n")
        if not user_choise.isdigit() or int(user_choise) not in range(1, len(wgs) + 1):
            user_choise = 0
        else:
            user_choise = wgs[int(user_choise) - 1]
        wages[emp[i]] = user_choise
    return wages


def wage_result(wgs_data, favs, coef_emp, coef_favs):
    '''
    Generates final document with actual wages

    :param wgs_data: takes dictionary with keys: employers, items: wages
    :param favs: takes list with favourite employers
    :param coef_emp: takes coefficient for employers wage
    :param coef_favs: takes coefficient for favourite employers wage
    :return: sorted dictionary with actual wages(with coefficient influence) and favourite employers in UPPERCASE
    '''
    for i in wgs_data.keys():
        if i in favs:
            wgs_data[i] = int(wgs_data[i] * coef_favs)
        else:
            wgs_data[i] = int(wgs_data[i] * coef_emp)
    for i in favs:
        wgs_data[i.upper()] = wgs_data.pop(i)
    wgs_data = dict(sorted(wgs_data.items(), key=lambda x: x[0]))  # sort dictionary by alphabet(in fact by UTF-8 :))
    return wgs_data


def print_wages_list(dct, entry_string):
    '''
    Prints wage list to console

    :param dct: takes wage list
    :param entry_string: takes first string to final document
    :return: wage list in console
    '''
    print(f'{entry_string}')
    for i in dct.keys():
        print(f'{i}: {dct[i]}')


data_emp = employers_data(5)
data_wage = wage_data(data_emp)
wage_list = wage_common(emp=data_emp, wgs=data_wage)
print_wages_list(wage_list, 'Standart wages list')
result_wage = wage_result(wage_list, favorits_list(data_emp), 1.5, 2)
print_wages_list(result_wage, 'Final wages list 12.2022')
