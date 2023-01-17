from typing import Dict, Iterable


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class CourseGrades:
    def __init__(self, course_name: str, grades: Iterable[float] = []) -> None:
        self.course_name: str = course_name
        self.grades: list[float] = grades

    def add_grades(self, *grades: float):
        self.grades.extend(grades)


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.courses: Dict[str, CourseGrades] = {}

    def add_grades(self, *courses: CourseGrades):
        for course in courses:
            if course.course_name in self.courses:
                self.courses[course.course_name].grades.extend(course.grades)
            else:
                self.courses[course.course_name] = course

    def get_courses(self):
        return self.courses

    def get_average_by_course(self, course_name: str) -> float:
        result = 0.0
        if course_name in self.courses:
            sum = 0.0
            for grade in self.courses[course_name].grades:
                sum += grade
            result = sum / len(self.courses[course_name].grades)
        return result


math = CourseGrades('math')
math.add_grades(6, 8)
physics = CourseGrades('physics', [8, 10])
chemistry = CourseGrades('chemistry', [6])

stud = Student('Vio', 35)
stud.add_grades(math, physics)
stud.add_grades(chemistry)

print(stud.get_average_by_course('math'))
