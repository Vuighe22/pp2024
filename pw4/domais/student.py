# class for Students
class Student:
    def __init__(self, name, id, DoB):
        self.__Name = name
        self.__IDStudent = id
        self.__DoB = DoB
        self.__GPA = 0

    def get_Namest(self):
        return self.__Name

    def get_IDStudent(self):
        return self.__IDStudent

    def get_formattedDoB(self):
        return f"{self.__DoB[0]}/{self.__DoB[1]}/{self.__DoB[2]}"
    
    def set_GPA(self,gpa):
        self.__GPA = gpa

    def __str__(self):
        return f"_ Full name: {self.__Name}\n_ ID of Student: {self.__IDStudent}\n_ Date of birth: {self.get_formattedDoB()}\n_ GPA: {self.__GPA}"

