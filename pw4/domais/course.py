# class for Course
class Course:
    def __init__(self, name, id, credits):
        self.__Name = name
        self.__IDCourse = id
        self.__Credit = credits

    def __str__(self):
        return f'_ Name course: {self.__Name}\n_ ID of course: {self.__IDCourse}\n_ Credit: {self.__Credit}'

    def get_NameCs(self):
        return self.__Name

    def get_IDCourse(self):
        return self.__IDCourse
    
    def get_Credit(self):
        return self.__Credit

