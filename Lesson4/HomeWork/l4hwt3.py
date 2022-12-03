# 3 - В файле, содержащем фамилии студентов и их оценки,
# изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.

from gbfunctions import give_int


def create_file(amnt: int) -> str:
    '''
    Creates .txt file with lines filled by student's names and grades

    :param amnt: amount of students
    :return: name of the file
    '''

    with open('students_and_grades.txt', 'w', encoding='UTF8') as file:
        for _ in range(amnt):
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
    return 'students_and_grades.txt'


def edit_file(file_name: str, grade: int) -> str:
    '''
    Edit student names from "file_name" file to upper case if their grade higher
    then "grade" parameter.

    :param file_name: name of file, that we try to edit
    :param grade: student's grade
    :return: name of edited file
    '''

    with open(file_name, 'r', encoding='UTF8') as file:
        lines_data = []
        for line in file.readlines():
            data_string = line.strip('\n')
            student_grade = int(data_string[-1])
            if student_grade >= grade:
                lines_data.append(data_string.upper() + '\n')
            else:
                lines_data.append(data_string + '\n')
    with open(file_name, 'w', encoding='UTF8') as file:
        for i in lines_data:
            file.write(i)
    return file_name


amount = give_int('Type amount of students: ', 1)
fl_name = create_file(amount)
result_file = edit_file(fl_name, 4)
print(f'You can see your work in {result_file}')
