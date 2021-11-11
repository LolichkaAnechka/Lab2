# The class GROUP contains a sequence of instances of the class STUDENT. 
# The class STUDENT contains the student's name, surname, record book number and grades. 
# Determine the required attributes-data and attributes-methods in classes GROUP and STUDENT. 
# Find the average score of each student. Output to the standard output stream the five students with the highest average score.
# Assume *that there can be no more than 20 students in a group, as well as students with the same name and surname.

class Student:
    
    name:str
    surname:str
    number:int
    grades:list[int]
    average: int

    def __init__(self, new_name, new_surname, new_number, new_grades):
        if not (isinstance(new_name, str) and isinstance(new_surname, str)
                and isinstance(new_number, int) and all(isinstance(grades, int) for grades in new_grades)):
            raise TypeError("Wrong Value Type")
        self.name = new_name
        self.surname = new_surname
        self.number = new_number
        self.grades = new_grades


    def __str__(self) -> str:
        return f"\n{self.surname} {self.name} \nRecord book number: {str(self.number)}\
                 \nGrades: {' '.join(map(str, self.grades))}\
                \nAverage score: {str(self.average)} \n"


    def __eq__(self, other) -> bool:
        if self.name == other.name and self.surname == other.surname:
            return True
        return False

    def __lt__(self, other) -> bool:
        return self.average < other.average

    def __gt__(self, other) -> bool:
        return self.average > other.average

    @property
    def average(self):
        return sum(self.grades)/len(self.grades)


class Group:
    MAX_STUDENTS = 20
    list_of_students = []
    def __init__(self, *args:Student):
        if not all(isinstance(x, Student) for x in args):
            raise TypeError("Wrong Value Type")
        for student in args:
            if self.__check(student) and len(self.list_of_students)<self.MAX_STUDENTS:
                self.list_of_students.append(student)
            
        
    def __check(self, student_to_check:Student) -> bool:
        for student in self.list_of_students:
            if student == student_to_check:
                return False
        return True


    def __top5(self):
        # return sorted(self.list_of_students, key=lambda x: x.average ,reverse=True)[:5]
        return sorted(self.list_of_students, reverse=True)[:5]


    def best_students(self):
        return ''.join(map(str, self.__top5()))


slava = Student("Slava", "Moskalenko", 17, (5, 5))
slava1 = Student("Slava", "Moskalenko", 18, (4, 4))
person15 = Student("Alex", "Mos", 10, (3, 3))
person16 = Student("Anthony", "Moskalenko", 16, (2, 2))
person17 = Student("Anthony", "Moskalenk", 15, (1, 1))
person18 = Student("Anthony", "Moskalen", 14, (4, 5))
person19 = Student("Anthony", "Moskale", 13, (3, 4))
person20 = Student("Anthony", "Moskal", 12, (2, 3))
person21 = Student("Anthony", "Moska", 11, (1, 2))
group = Group(slava, slava1, person21, person20, person19, person18, person17, person16, person15)
print(group.best_students())