from fileinput import close
from typing import List
from xml.etree.ElementInclude import DEFAULT_MAX_INCLUSION_DEPTH

username1 = "shiva"
password1 = "python"

for i in range(0,3):
     username = input("enter username\n")
     password = input("enter password\n")
     if username == username1 and password == password1:
         print("you are successfully login\n")
         print("\t\t*****welcome to employee management*****\t\t")

     else:
         print("invalid credential")




class Employee:
    employeelist = list()

    
    def __init__(self, empNo, empName, empDes, empSal,asal):
    
        file = open("emp.txt", "a+")
        # file.write( empNo + "\t"  + empName+ "\t" + empDes + "\t" + empSal + "\n")


        self.empNo, self.empName, self.empDes, self.empSal,self.asal = empNo, empName, empDes, empSal,asal
        file.close()


    def addNewEmployee(self):
        

        Employee.employeelist.append(self)
        


    def getEmplist(self):
        file = open("emp.txt", "r+")
        for line in file:
            print(line)
        return Employee.employeelist
        file.close()


    def getEmpById(self, empNo):
        file = open("emp.txt" , "r")
        c = file.readlines()
        print(c)

        for emp in Employee.employeelist:
            if emp.getEmpNo(empNo) == emp.empNo:
                return emp
        return False
        file.close()

    def  updateEmployeeById(self,empNo,empName,empDes,empSal,asal):  
        for emp in Employee.employeelist:
            if(emp.getEmpNo(empNo) == emp.empNo):
                emp.empNo,emp.empName,emp.empDes,emp.empSal,emp.asal =empNo,empName,empDes,empSal,asal
                return True
        return False      

    def removeEmpById(self,empNo):
        for emp in Employee.employeelist:
            if(emp.getEmpNo(empNo) == emp.empNo):
                Employee.employeelist.remove(emp)
                return True
        return False        

    def setEmpNo(self, empNo):
        self.empNo = empNo

    def getEmpNo(self, empNo):
        return self.empNo

    def setEmpName(self, empName):
        self.empName = empName

    def getEmpName(self, empName):
        return self.empName

    def setEmpDes(self, empDes):
        self.empDes = empDes

    def getEmpDes(self, empDes):
        return self.empDes

    def setEmpSal(self, empSal):
        self.empSal = empSal

    def getEmpSal(self, empSal):
        return self.empSal

    def setEmpasal(self, asal):
        self.asal = asal

    def getEmpasal(self, asal):
        return self.asal

    def __str__(self):
        return "%d %s %s %d %f" % (self.empNo, self.empName, self.empDes, self.empSal,self.asal)


choice = 1
employee = Employee(0, "", "", 0,0.0)

while choice!=0:
    print("\n1.add employee\n2.view employee\n3.serach employee\n4.update employee \n5.delete employee\n6.exit")
    choice = int(input("enter your choice"))
    if(choice == 1):
       empNo = int(input("enter emplyee number\n"))
       empName = str(input("enter emplyee name\n"))
       empDes = str(input("enter emplyee Description\n"))
       empSal = int(input("enter emplyee monthly salary\n"))
       days=int(input("enter employee working days"))
       a=empSal/30
       asal=a*days


       emp = Employee(empNo, empName, empDes, empSal,asal)
       emp.addNewEmployee()
       print("record added Successfully")

    elif(choice == 2):
        print("\n")

        for emp in employee.getEmplist():
            print(emp)
            print("record view successfully")
    elif(choice == 3):
           empNo = int(input("enter emplyee number"))
           emp = employee.getEmpById(empNo)
           if(emp==False):
               print("\n no record found for id:",empNo)
           else:
            print(emp) 
    elif(choice==4):
         empNo = int(input("enter emplyee number"))
         empName = str(input("enter emplyee name"))
         empDes = str(input("enter emplyee Description"))
         empSal = int(input("enter emplyee salary"))
         emp=employee.updateEmployeeById(empNo,empName,empDes,empSal,asal)
         if(emp==False):
               print("\n no update found for id:",empNo)
         else:
            print("Successfully Updated employee information for id",empNo) 
    elif(choice == 5):
         empNo = int(input("enter emplyee number"))
         emp=employee.removeEmpById(empNo)
         if(emp==False):
               print("\n no record found for id:",empNo)
         else:
            print("Successfully remove employee information for id",empNo) 
    elif(choice==6):
          print("exiting")