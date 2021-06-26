class Students:

    def __init__(self, rollno, phoneno, grade, name):
        self.rollno=rollno
        self.phoneno=phoneno
        self.grade=grade
        self.name=name
        print('Student details added.\n')

    def description(self):
        print('Description:')
        print('Name -',self.name,'\nRoll No -',self.rollno,'\nPhone No -',self.phoneno,'\nGrade -',self.grade,('\n'))

    def changephone(self,phoneno):
        self.phoneno=phoneno
        print('New Phone No -',self.phoneno)

class Sports(Students):

    def __init__(self, rollno, phoneno, grade, name, sport):
        self.rollno=rollno
        self.phoneno=phoneno
        self.grade=grade
        self.name=name
        self.sport=sport
        print('Students Sports details added.\n')

    def favsports(self):
        print('The student plays ',self.sport,'\n')

    def changesport(self,sport):
        self.sport=sport
        print('New Sport -',self.sport,'\n')

    def __del__(self):
        print('Student doesnt play sports anymore\n')

student1=Students(1,'7306128735',12,'John')
student1.description()
student1=Sports(1,'7306128735',12,'John','Football')
student1.favsports()
student1.changephone('9361829673')
student1.changesport('Tennis')
del student1

