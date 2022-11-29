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

def employers_data(num: int) -> list:
    '''
    Generates list for employers at company.

    :param num: takes amount of employers
    :return: employers list
    '''
    names = [input('Type name of employer: ') for i in range(num)]
    return names


def salary_data(emp: list) -> list:
    '''
    Generates list for employer's salary. List length can't be larger than employers list.

    :param emp: employers list
    :return: salaries list
    '''
    salaries = []
    for i in range(len(emp)):
        val = ''
        while not val.isdigit():
            val = input('Type salary value: ')
            if val.isdigit() and int(val) > 0:
                salaries.insert(i, int(val))
            else:
                print('Type natural number pls. They working not for food or letters')
    return salaries


def favorits_list(emp: list) -> list:
    '''
    Gives Lyuba opportunity to choose bosses favourites from employers list.

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


def salary_common(emp: list, slr: list) -> dict:
    '''
    Generates dictionary with "employer - salary" dependance where salary is chosen by Lyuba.

    :param emp: takes list of employers
    :param slr: takes list of employer's salaries
    :return: dictionary with emp values as keys, and slr values as items
    '''
    salaries = {}
    for i in range(len(emp)):
        user_choise = input(f"What salary's value is for {emp[i]}?\n" \
                            f"Choice right position from following list:\n{slr}\n" \
                            f"Type position from 1 to {len(slr)}:\n")
        if not user_choise.isdigit() or int(user_choise) not in range(1, len(slr) + 1):
            user_choise = 0
        else:
            user_choise = slr[int(user_choise) - 1]
        salaries[emp[i]] = user_choise
    return salaries


def salary_result(slr_data: dict, favs: list, coef_emp: float, coef_favs: float) -> dict:
    '''
    Generates final document with actual salaries.

    :param slr_data: takes dictionary with keys: employers, items: salaries
    :param favs: takes list with favourite employers
    :param coef_emp: takes coefficient for employers salary
    :param coef_favs: takes coefficient for favourite employers salary
    :return: sorted dictionary with actual salaries(with coefficient influence) and favourite employers in UPPERCASE
    '''
    for i in slr_data.keys():
        if i in favs:
            slr_data[i] = int(slr_data[i] * coef_favs)
        else:
            slr_data[i] = int(slr_data[i] * coef_emp)
    for i in favs:
        slr_data[i.upper()] = slr_data.pop(i)
    slr_data = dict(sorted(slr_data.items(), key=lambda x: x[0]))  # sort dictionary by alphabet(in fact by UTF-8 :))
    return slr_data


def print_salaries_list(dct, entry_string: str) -> None:
    '''
    Prints salary list to console.

    :param dct: takes salary list
    :param entry_string: takes first string to final document
    :return: salary list in console
    '''
    print(f'{entry_string}')
    for i in dct.keys():
        print(f'{i}: {dct[i]}')


data_emp = employers_data(5)
data_salary = salary_data(data_emp)
salary_list = salary_common(emp=data_emp, slr=data_salary)
print_salaries_list(salary_list, 'Standart salaries list')
result_salary = salary_result(salary_list, favorits_list(data_emp), 1.5, 2)
print_salaries_list(result_salary, 'Final salaries list 12.2022')
