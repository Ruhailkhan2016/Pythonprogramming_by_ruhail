class EmpPersonalInfo:  #parent class

    def printDetails(self):

        print(f"Employee Name is : {self.empName} \nEnployee ID is : {self.empID}")


class Salary(EmpPersonalInfo): #child class inherit parent class properties

    def CalculateSalary(self):

        onedaysalary = self.basicsalary/30
        workingdays = 30-self.leave
        totalsalary = onedaysalary*workingdays

        print("Your Salary is : ", totalsalary)


ruhail = Salary()
basicsalary = float(input("Enter Basicsalary : "))
ruhail.basicsalary = basicsalary  

leave = int(input("Enter No. of Leave : "))
ruhail.leave = leave

empName = input("Enter your Name : ")
ruhail.empName = empName

empID = int(input("Enter Employee ID : "))
ruhail.empID = empID
print()
print()
print()
ruhail.printDetails()
ruhail.CalculateSalary()