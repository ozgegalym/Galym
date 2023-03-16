# Создание словаря с данными о различных студентах
students = {
    'Bauka': {
        'age': 20,
        'major': 'Computer Science',
        'gpa': 3.12
    },
    'Aigerim': {
        'age': 20,
        'major': 'Computer Science',
        'gpa': 3.59
    },
    'Uldana': {
        'age': 19,
        'major': 'Computer Science',
        'gpa': 2.86
    }
}

# # Использование метода keys() для получения списка ключей словаря
# print("Ключи словаря студент:")
# print(students.keys())
# print()

#  # Использование метода values() для получения списка значений словаря
# print("значение словаря студент:")
# print(students.values())
# print()

 # Использование метода items() для получения списка пар ключ-значение словаря
# print(students.items())
# print()

#  # Использование метода get() для получения значения по ключу, с возможностью задать значение по умолчанию
# print("Возраст Улданы:", students.get('Uldana')['age'])
# print("Что то  Улданы ('-'):", students.get('Uldana').get('=', '-'))
# print()

 # Использование метода pop() для удаления элемента по ключу, с возможностью задать значение по умолчанию
# removed_student = students.pop('Aigerim', None)
# if removed_student:
#      print("Удаленный студент Айгерим:", removed_student)
# print()

#  students.clear()
#  print("Cleared students dictionary:", students)

