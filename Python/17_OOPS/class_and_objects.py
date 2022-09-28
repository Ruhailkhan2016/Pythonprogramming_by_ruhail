# class is a group of element having common properties and behaviours. and class is a blue print or we can class is a collection of objects or we say class is a template

class Student:

    def studentInfo(self):

        print("Your name is : ", self.name)
        print("Your roll no. is : ", self.rollno)
    



# object is a instance of a class, we can multiple objects as our requirements
rahul = Student()

rahul.name = "Rahul"
rahul.rollno = "001"
rahul.studentInfo()

print()
Ruhail = Student()

Ruhail.name = "Ruhail Khan"
Ruhail.rollno = "002"
Ruhail.studentInfo()


        