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
        self.course = current_year - (self.year_of_birth + 15)

        if self.course > 4:
            return "College completed"
        elif self.course < 1:
            return "Ще не студент"
        else:
            return self.course

    def name_surname_list(self):
        return [self.name, self.surname]

student = Nazar("Назар", "Синиця", 2008)
print("Курс:", student.return_course())
print("Ім'я та прізвище:", student.name_surname_list())
