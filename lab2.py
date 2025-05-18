from datetime import datetime

class Nazar:
    def __init__(self, name=None, surname=None, year_of_birth=None):
        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth
        self.course = None

    def return_course(self):
        if self.year_of_birth is None:
            return "Рік народження не вказано"

        current_year = datetime.now().year

        year_of_start = self.year_of_birth + 15

        self.course = current_year - year_of_start

        if self.course > 4:
            return "College completed"
        elif self.course < 1:
            return "Ще не студент"
        else:
            return self.course

    def name_surname_list(self):
        return [self.name, self.surname]

class Student(Nazar):
    def __init__(self, name=None, surname=None, year_of_birth=None,
                 specialty=None, group=None, average_score=None):
        super().__init__(name, surname, year_of_birth)

        self.specialty = specialty
        self.group = group
        self.__average_score = average_score

    def __has_scholarship(self):
        if self.__average_score is None:
            return "Оцінка не вказана"
        return self.__average_score >= 8.0

    def get_student_status(self):
        if self.__has_scholarship():
            return f"{self.name} отримує стипендію"
        else:
            return f"{self.name} не отримує стипендію"

    def _full_info(self):
        return f"{self.name} {self.surname}, курс: {self.return_course()}, група: {self.group}, спец: {self.specialty}"

student = Student("Назар", "Синиця", 2008, "ІСТ", "22", 8.5)

print("Курс:", student.return_course())
print("ПІБ:", student.name_surname_list())
print("Стипендія:", student.get_student_status())
print("Інформація:", student._full_info())
