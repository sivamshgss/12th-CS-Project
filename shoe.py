import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='root',database='shoe_billing')
if conn.is_connected():
   print('connected sucessfully')
conn.autocommit=True
c1=conn.cursor()
c1.execute("create table shoe_details(shoe_code int primary key,brand_name varchar(25),customer_name varchar(25),\
customer_number int,customer_address varchar(25),amount int)")
c1=conn.cursor()
print("                  shoe billing")
print("                               ")
print("1:ENTER CUSTOMER DETAILS")
print("                          ")
print("2:SHOW CUSTOMERS DETAILS")
print("                            ")
w=1
while w==1:
      v_choice=int(input("enter the choice: "))
      if v_choice==1 :
            code=input("enter code=")
            brand =input("enter brand=")
            name=input("enter customer name=")
            number=input("enter  phone number=")
            details=input ("adress=")
            amount=input("amount=")
            c1.execute("insert into shoe_details values ("+code+",'"+brand+"'"+",'"+name+"',"+number+",'"+details+"',"+amount+")")
            conn.commit()
            print('database updated')
      else:
            try:
                  v_choice==2
                  v_code=input("enter the code number: ")
                  c1.execute("select * from shoe_details where shoe_code ="+v_code)
                  data=c1.fetchall()
                  print("Shoe code:",data[0][0])
                  print("brand name:",data[0][1])
                  print("customer name:",data[0][2])
                  print("customer number:",data[0][3])
                  print("customer detail:",data[0][4])
                  print("amoumt:",data[0][5])
            except:
                  print('invalid code')
      w=int(input('Press 1 to try again, 0 to exit: '))
print('Thank You')
