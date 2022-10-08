# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0
def compare_files_by_rows(file1, file2):
    return sum(1 for line in open(file1, 'r')) == sum(1 for line in open(file2, 'r'))


def addition_from_file(file1, file2):
    new_data = []
    with open(file1, 'r', encoding="UTF-8") as output1:
        with open(file2, 'r', encoding="UTF-8") as output2:
            for i in range(1, sum(1 for line in output2)):
                new_line = output1.readline(i).strip('=0') + output2.readline(i)
                new_data.append(new_line)
    with open(file1, 'w', encoding="UTF-8") as output:
        for i in range(len(new_data)):
            output.write(f'{new_data[i]}\n')
    return

first_file = input('Enter name of the first file: ')
second_file = input('Enter name of the second file: ')
if compare_files_by_rows(first_file, second_file):
    addition_from_file(first_file, second_file)
else:
    print("Data in files don't match!")
