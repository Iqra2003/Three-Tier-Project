import pyodbc

def getConnection():
    cnxn=pyodbc.connect(r'Driver=SQL Server; Server=FARHEEN\SQLEXPRESS;Database=iqra;')
    cursor=cnxn.cursor()
    return cursor

def FetchAllEmployees():
    cur = getConnection()
    cur.execute("select * from tblemp")
    rows=cur.fetchall()
    return rows

def dataInsertion(a):
    cur=getConnection()
    cr=cur.execute(f"insert into tblemp values({a.id},'{a.name}','{a.city}',{a.salary})")
    cur.commit()
    return (cr)

def dataUpdation(e):
    cur=getConnection()
    cr=cur.execute(f"update tblemp set name='{e.name}' where id = {e.id}")
    cur.commit()
    return (cr)

def dataDeletion(t):
    cur=getConnection()
    cr=cur.execute(f"delete from tblemp where id={t.id}")
    cur.commit()
    return (cr)
