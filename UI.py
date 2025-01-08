import BLL

userInput=input("press 'F' to fetch data, press 'I' to insert data,press 'U' to update data and press 'D' to delete data from table")
if userInput=='F':
    objemp=BLL.Employee()
    rows=objemp.getAllEmployees()
    print(rows)
    
elif userInput=='I':
    id=int(input("enter ID:"))
    name=input("enter name:")
    city=input("enter city:")
    salary=int(input("enter salary:"))
    
    empobj=BLL.Employee(id,name,city,salary)
    r=empobj.insertdata()
    print(empobj.getAllEmployees())
    
elif userInput=='U':
    id=int(input("enter ID"))
    name=input("enter name")

    obj=BLL.Employee(id,name)
    s=obj.updatedata()
    print(obj.getAllEmployees())


elif userInput=='D':
    id=int(input("enter ID"))

    obj=BLL.Employee(id)
    j=obj.deletedata()
    print(obj.getAllEmployees())
