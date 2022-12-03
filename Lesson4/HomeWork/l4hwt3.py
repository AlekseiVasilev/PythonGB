# 3 - В файле, содержащем фамилии студентов и их оценки,
# изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.

from gbfunctions import give_int
from os import path


def create_file() -> None:
    '''
    Creates .txt file with lines filled by student's names and grades

    :return: info about operation
    '''

    amount = give_int('Type amount of students: ', 1)
    with open('students_and_grades.txt', 'w', encoding='UTF8') as file:
        for _ in range(amount):
            name = input("Type student's name: ")
            file.write(f'{name} ')
            while True:
                grade = input(f"Type grade for {name}: ")
                if grade.isdigit() and 0 < int(grade) <= 5:
                    file.write(f'{grade}\n')
                    break
                else:
                    print('Type integer number from 1 to 5, please')
                    continue
    return print("Success!\nYou have created students_and_grades.txt\n")


def edit_file(file_name: str, grade: int) -> None:
    '''
    Edit student names from "file_name" file to upper case if their grade higher
    then "grade" parameter.
    Important: student's grate must be last symbol in line of the file!!!

    :param file_name: name of file, that we try to edit
    :param grade: student's grade
    :return: info about operation
    '''

    with open(file_name, 'r', encoding='UTF8') as file:
        lines_data = []
        for line in file.readlines():
            data_string = line.strip('\n')
            try:
                student_grade = int(data_string[-1])
            except ValueError:
                exit(f"Error: 0x80002020 Student's grade is missing.\n"
                     f"Try to edit {file_name} manually or contact your system administrator.")
            if student_grade >= grade:
                lines_data.append(data_string.upper() + '\n')
            else:
                lines_data.append(data_string + '\n')
    with open(file_name, 'w', encoding='UTF8') as file:
        for i in lines_data:
            file.write(i)
    return print("Success!\nYou have edited students_and_grades.txt\n")


def menu_input():
    '''
    Creates console menu for user

    :return:
    '''

    while True:
        print('Type "1" if you want to create new file')
        print('Type "2" if you want to edit existing file')
        print('Type "-1" if you want to exit')
        num = input('What operation do you want to do?: ')
        if num == '1':
            create_file()
        elif num == '2':
            if path.exists(fr'.\students_and_grades.txt'):
                edit_file('students_and_grades.txt', 4)
            else:
                print('File students_and_grades.txt is not exist in this folder.')
                print("Would you like to create file? (Y/N)")
                if input().lower() in ('y', 'ye', 'yes'):
                    create_file()
                else:
                    print("Create file students_and_grades.txt and put it to root folder\n")
        elif num == '-1':
            return exit(print("Bye-bye"))
        else:
            print("Incorrect value, try again!")


menu_input()
