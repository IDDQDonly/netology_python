class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        complete_str =(f"Имя: {self.name} \n"
                       f"Фамилия: {self.surname}\n"
                       f"Средняя оценка за домашнее задание: {self.get_average_grade()}\n"
                       f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                       f"Завершенные курсы: {', '.join(self.finished_courses)}"
                       )
        return complete_str

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() != other.get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() >= other.get_average_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() > other.get_average_grade()

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self) -> float:
        all_grades = []
        for value in self.grades.values():
            all_grades += value
        if all_grades:
            return round(sum(all_grades) / len(all_grades), 2)
        return 0

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_grade()}"

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() != other.get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() >= other.get_average_grade()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() > other.get_average_grade()

    def get_average_grade(self)-> float:
        all_grades = []
        for value in self.grades.values():
            all_grades += value
        average = round(sum(all_grades) / len(all_grades),2)
        return average

class Reviewer(Mentor):
    def rate_hw(self, student, course: str, grade: int):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"

def get_average_grade_for_students(students: list, course: str)-> float:
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades += student.grades[course]
    return round(sum(all_grades) / len(all_grades), 2)

def get_average_grade_for_lecturer(lecturers: list, course: str)-> float:
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades += lecturer.grades[course]
    return round(sum(all_grades) / len(all_grades), 2)

# Создаем экземпляры классов
# Student_1
student_1 = Student('Pavel', 'Pavlov', 'm')
student_1.finished_courses += ['Git', 'SQL', 'Java']
student_1.courses_in_progress += ['Python', 'C++']

# Student_2
student_2 = Student('Ivan', 'Ivanov', 'm')
student_2.finished_courses += ['Bash', 'SQL', 'Java']
student_2.courses_in_progress += ['Python', 'Kotlin']

# Lecturer_1
lecturer_1 = Lecturer('Petr', 'Petrov')
lecturer_1.courses_attached += ['Python', 'C++']

# Lecturer_2
lecturer_2 = Lecturer('Kirill', 'Kirillov')
lecturer_2.courses_attached += ['Python', 'Kotlin']

# Reviewer_1
reviewer_1 = Reviewer('Vlad', 'Vladov')
reviewer_1.courses_attached += ['Python', 'C++']

# Reviewer_2
reviewer_2 = Reviewer('Dmitry', 'Dmitriev')
reviewer_2.courses_attached += ['Python', 'Kotlin']

# Добавляем оценки student
student_1.rate_lecture(lecturer_1, 'Python', 4)
student_1.rate_lecture(lecturer_1, 'C++', 4)
student_1.rate_lecture(lecturer_2, 'Python', 4)
student_1.rate_lecture(lecturer_2, 'Kotlin', 4)

student_2.rate_lecture(lecturer_1, 'Python', 6)
student_2.rate_lecture(lecturer_1, 'C++', 6)
student_2.rate_lecture(lecturer_2, 'Python', 8)
student_2.rate_lecture(lecturer_2, 'Kotlin', 8)

# Добавляем оценки reviewer
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'C++', 10)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'C++', 9)

reviewer_2.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_1, 'C++', 8)
reviewer_2.rate_hw(student_2, 'Python', 6)
reviewer_2.rate_hw(student_2, 'C++', 7)

# Сравнение студентов
print('----------------------------------------------')
print(f"Сравнение студентов: {student_1 > student_2}")
print(f"Сравнение лекторов: {lecturer_1 > lecturer_2}")
print(f"Сравнение студентов: {student_1 < student_2}")
print(f"Сравнение лекторов: {lecturer_1 < lecturer_2}")
print(f"Сравнение студентов: {student_1 >= student_2}")
print(f"Сравнение лекторов: {lecturer_1 >= lecturer_2}")
print(f"Сравнение студентов: {student_1 <= student_2}")
print(f"Сравнение лекторов: {lecturer_1 <= lecturer_2}")
print(f"Сравнение студентов: {student_1 != student_2}")
print(f"Сравнение лекторов: {lecturer_1 != lecturer_2}")
print('----------------------------------------------')
# Списки студентов и лекторов
students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]
# Средние оценки студентов и лекторов
print(f"Средняя оценка студентов по курсу Python: {get_average_grade_for_students(students, 'Python')}")
print(f"Средняя оценка лекторов по курсу Python: {get_average_grade_for_lecturer(lecturers, 'Python')}")
print('----------------------------------------------')
# print student_1
print(student_1)
print('----------------------------------------------')
# print student_2
print(student_2)
print('----------------------------------------------')
# print lecturer_1
print(lecturer_1)
print('----------------------------------------------')
# print lecturer_2
print(lecturer_2)
print('----------------------------------------------')
# print reviewer_1
print(reviewer_1)
print('----------------------------------------------')
# print reviewer_2
print(reviewer_2)
print('----------------------------------------------')

