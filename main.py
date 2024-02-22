import csv

# with open('students.csv') as file:
#     sum_score = {}
#     count_scores = {}
#     k = 0
#     reader = list(csv.reader(file, delimiter=','))[1:]
#     print('10 класс:')
#     for i_d, name, titleProject_id, klass, score in reader:
#         if 'Хадаров Владимир' in name:
#             print(f'Ты получил: {score}, за проект - {titleProject_id}')
#         sum_score[klass] = sum_score.get(klass, 0) + (int(score) if score != 'None' else 0)
#         count_scores[klass] = count_scores.get(klass, 0) + 1
#
#         if '10' in klass:
#             k += 1
#             name1 = name.split()
#             print(f'{k} место: {name1[1][0]}. {name1[0]}')
#
#             if k == 3:
#                 break
#
#     for line in reader:
#         if line[-1] == 'None':
#             line[-1] = round(sum_score[line[-2]] / count_scores[line[-2]], 3)

# with open('students_new.csv', 'w') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
#     writer.writerows(reader)


# with open('students.csv') as file:
#     reader = csv.DictReader(file, delimiter=',')
#     reader = list(reader)
#
#     for i in range(len(reader)):  # Изменяем None на 0
#         if reader[i]['score'] == 'None':
#             reader[i]['score'] = '0'
#
#     for i in range(len(reader)):  # Сортировка вставками
#         current_person = reader[i]
#         j = i
#         while j > 0 and int(reader[j - 1]['score']) < int(current_person['score']):
#             reader[j] = reader[j - 1]
#             j -= 1
#         reader[j] = current_person
#
#     count_of_best_ten_grade = 0
#
#     print('10 класс:')
#
#     for i in range(len(reader)):
#         if '10' in reader[i]['class']:
#             count_of_best_ten_grade += 1
#             name_fi = reader[i]['Name'].split()
#             print(f'{count_of_best_ten_grade} место: {name_fi[1][0]}. {name_fi[0]}')
#         if count_of_best_ten_grade == 3:
#             break
# with open('students.csv') as file:
#     reader = csv.DictReader(file, delimiter=',')
#     reader = list(reader)
#     request = input()
#     while request != 'СТОП':
#         is_real_project = False
#         for i in range(len(reader)):
#             if reader[i]['titleProject_id'] == request:
#                 project_id = reader[i]['titleProject_id']
#                 name = reader[i]['Name'].split()
#                 score = reader[i]['score']
#                 print(f'Проект № {project_id} делал: {name[1][0]}. {name[0]} он(а) получил(а) оценку - {score}')
#                 is_real_project = True
#                 break
#         if not is_real_project:
#             print('Ничего не найдено')
#         request = input()
# import random
# from string import ascii_letters, digits
#
#
# def create_password():
#     letter_digit = ascii_letters + digits
#     password = ''.join(random.choices(letter_digit, k=8))
#     return password
#
#
# def create_login(name):
#     name = name.split()
#     return f'{name[0]}_{name[1][0]}{name[2][0]}'
#
#
# with open('students.csv') as file:
#     reader = csv.DictReader(file, delimiter=',')
#     reader = list(reader)
#     for person in reader:
#         person['login'] = create_login(person['Name'])
#         person['password'] = create_password()
#
# with open('students_password.csv', 'w') as file:
#     names = ['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password']
#     writer = csv.DictWriter(file, fieldnames=names)
#     writer.writerows(reader)

import csv


def hash(s):
    """
    Описание
    :param s: строка, в
    :return:
    """
    p = 67
    m = 10 ** 9 + 9  # это взяла из задания
    alph = ''.join([chr(i) for i in range(ord('А'), ord('я') + 1)])
    alph += 'ёЁ '
    hash_code = 0
    j = 0
    for i in s:
        hash_code += ((alph.index(i) + 1) * p ** j) % m
        j += 1
    return hash_code


students_with_hash = []
with open('students.csv', encoding='utf-8') as f:
    reader = list(csv.DictReader(f, delimiter=','))
    for row in reader:
        row['id'] = hash(row['Name'])
        students_with_hash.append(row)
with open('student+_with_hash.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score'])
    writer.writeheader()
    writer.writerows(students_with_hash)
