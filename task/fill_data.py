from datetime import datetime
import faker
from random import randint
import sqlite3

NUMBER_STUDENTS = 50
NUMBER_LECTURERS = 5
NUMBER_GROUPS = 3
NUMBER_CLASSES = 8


def generate_fake_data(number_students, number_lecturers,
                       number_groups, number_classes) -> tuple():
    fake_students = []
    fake_lecturers = []
    fake_groups = []
    fake_classes = []

    '''Візьмемо три компанії з faker і помістимо їх у потрібну змінну'''
    fake_data = faker.Faker()

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_lecturers):
        fake_lecturers.append(fake_data.name())

    for _ in range(number_groups):
        fake_groups.append(fake_data.random_int())

    for _ in range(number_classes):
        fake_classes.append(fake_data.word())

    return fake_students, fake_lecturers, fake_groups, fake_classes


def prepare_data(students, lecturers, groups, classes) -> tuple():
    for_students = []
    for student in students:
        for_students.append((student, randint(1, NUMBER_GROUPS)))

    for_groups = []
    for group in groups:
        for_groups.append((group, ))

    for_lecturers = []
    for lecturer in lecturers:
        for_lecturers.append((lecturer, ))

    for_classes = []
    for cl in classes:
        for_classes.append((cl, randint(1, NUMBER_LECTURERS)))

    for_marks = []
    for st in range(1, NUMBER_STUDENTS + 1):
        for cl in range(1, NUMBER_CLASSES + 1):
            for _ in range(randint(1, 2)):
                mark_date = datetime(
                    2023, randint(1, 12), randint(1, 28)).date()
                for_marks.append((st, cl, randint(1, 5), mark_date))

    return for_students, for_lecturers, for_groups, for_classes, for_marks


def insert_data_to_db(students, lecturers, groups, classes, marks) -> None:

    with sqlite3.connect('university.db') as con:

        cur = con.cursor()

        sql_to_students = """INSERT INTO students(student, group_id)
                               VALUES (?, ?)"""

        cur.executemany(sql_to_students, students)

        sql_to_lecturers = """INSERT INTO lecturers(lecturer)
                                VALUES (?)"""
        cur.executemany(sql_to_lecturers, lecturers)

        sql_to_groups = """INSERT INTO groups(group_name)
                                VALUES (?)"""
        cur.executemany(sql_to_groups, groups)

        sql_to_classes = """INSERT INTO classes(class_name, lecturer_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_classes, classes)

        sql_to_marks = """INSERT INTO marks(
                              student_id, class_id, mark, date_of)
                              VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_marks, marks)

        con.commit()


if __name__ == "__main__":
    students, lecturers, groups, classes, marks = prepare_data(
        *generate_fake_data(
            NUMBER_STUDENTS, NUMBER_LECTURERS, NUMBER_GROUPS, NUMBER_CLASSES
        ))
    insert_data_to_db(students, lecturers, groups, classes, marks)
