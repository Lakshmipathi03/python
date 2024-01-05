import pymysql
con=pymysql.connect(user='root',password='root',port=3306,database='pythonmysql')
cursor=con.cursor()
def create_table():
    try:
        query='''
        create table customer1(
        id int primary key,
        name varchar(100),
        mobile bigint unique,
        balance bigint
        );
        '''
        cursor.execute(query)
    except pymysql.err.OperationalError as e:
        print(f'{e}')
def insert_record():
    query='''insert into customer1(id,name,mobile,balance)
    values('1','giri','9014672949','25000')'''
    cursor.execute(query)
    con.commit()

def get_record():
    query='select *from customer1'
    cursor.execute(query)
    records=cursor.fetchall()
    print(records)
def insert_dynamic(id,name,mobile,balance):
    record=(id,name,mobile,balance)
    query='insert into customer1(id,name,mobile,balance)values(%s,%s,%s,%s)'
    cursor.execute(query,record)
    con.commit()

     
def drop_record(cid):
    query=f"delete from customer1 where id={cid}"
    cursor.execute(query)
    con.commit()
    print('record removed')

    