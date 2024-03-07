# class for Mark
class Mark:
    def __init__(self, StudentIf, CourseIf, Mark):
        self.__StudentIf = StudentIf
        self.__CourseIf = CourseIf
        self.__Mark = Mark

    def get_Marks(self):
        return self.__Mark

    def get_StudentIf(self):
        return self.__StudentIf
    
    def get_Course(self):
        return self.__CourseIf

    def __str__(self) -> str:
        return f'___Student__ \n{self.__StudentIf}\n___Mark of course__\n{self.__CourseIf} : {self.__Mark}\n'

