import DBAL

class Employee():
    def __init__(self,id=0,name='noname',city='no city',salary=0):
        self.id=id
        self.name=name
        self.city=city
        self.salary=salary

    def getAllEmployees(self):
        employees=DBAL.FetchAllEmployees()
        return employees

    
    def insertdata(self):
        emp=DBAL.dataInsertion(self)
        return emp
    
    def updatedata(self):
        emp=DBAL.dataUpdation(self)
        return emp


    def deletedata(self):
        emp=DBAL.dataDeletion(self)
        return emp
        
