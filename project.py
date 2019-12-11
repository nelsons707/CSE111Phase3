import os
import sqlite3   ## Include SQLite package
import random

################ Connect SQLite Database ################

db_connection = None # Define the connection parameter
db_name = "project.db" # Specify the full path of Database file

try:
    db_connection = sqlite3.connect(db_name)
except sqlite3.Error as err: # If database connection failed this block of code  # handles the exception
    print(err)

if db_connection:
    print(db_connection) # Printing the connection object
    print("Successfully Established connection with SQLite3")
    print("\n\n")

################ Code ################

select_query = "SELECT * FROM region"

input_table = "CREATE TABLE warehouse( \
w_warehousekey decimal(3,0) not null,\
w_name char(25) not null,\
w_supplierkey decimal(2,0) not null,\
w_capacity decimal(6,2) not null,\
w_address varchar(40) not null,\
w_nationkey decimal(2,0) not null)"

#class data:
#  def __init__(self):
#      self.name=raw_input( "Enter Name: ")
#      self.supplier=raw_input( "Enter Supplier: ")
#      self.capacity=raw_input( "Enter Capacity: ")
#      self.address=raw_input( "Enter Address: ")
#      self.nation=raw_input( "Enter Nation: ")
#a=data()
#asking = input("Insert into warehouse (w_name,w_supplierkey,w_capacity,w_adress,w_nationkey) Values (?,?,?,?,?)",(a.name,a.supplier,a.capacity,a.address,a.nation))
#params = (name, supplier, capacity, address, nation)

db_cursor = db_connection.cursor()


def input_data():
    w_name=raw_input( "Enter Name: ")
    w_supplierkey=int(raw_input( "Enter Supplier: "))
    w_capacity=int(raw_input( "Enter Capacity: "))
    w_address=raw_input( "Enter Address: ")
    w_nationkey=int(raw_input( "Enter Nation: "))
    warehousekey = random.randint(1,100)
    db_cursor.execute("INSERT INTO warehouse(w_warehousekey, w_name, w_supplierkey, w_capacity, w_address, w_nationkey) VALUES(?,?,?,?,?,?)",(warehousekey, w_name, w_supplierkey, w_capacity, w_address, w_nationkey))
    db_connection.commit()

def query2():
    brewOrBlend=raw_input("What do you feel like drinking tonight? Enter beer or wine: ")
    
    if brewOrBlend == "beer" or brewOrBlend == "Beer":
        style=raw_input("What style of beer would you like? Enter Ale, Wheat Ale, Pilsner, Stout, or Lager seperated by a comma: \n")
        print("I want a " + style)
        db_cursor.execute("SELECT b_name FROM beer, TypesOfAlcohol WHERE a_beertypename = \"" + style + "\" AND a_typekey = b_typekey GROUP BY b_name;")
        db_connection.commit()
        result = db_cursor.fetchall()
        db_connection.commit()
        for row in result:
            print(row)
        
        drinkToFind = raw_input("If you would like to find locations where you can find a drink, please type in the drink name \n\n ")
        db_cursor.execute("SELECT l_name, l_address, l_phonenumber FROM location, foundat WHERE l_locationkey = f_locationkey AND f_beername LIKE'" + drinkToFind + "%';")
        db_connection.commit()
        result = db_cursor.fetchall()
        print("############# Locations ###############")
        for row in result:
            print(row)

    elif brewOrBlend == "wine" or breworBlend == "Wine":
        style = raw_input("What style of wine would you like? Enter Pinot Noir, Syrah, Cabernet Sauvigon, Red Blend, Chardonnay, Zinfandel, or Rose seperated by a comma \n\n")
        print("I want a " + style)
        db_cursor.execute("Select w_name FROM wine, TypesOfAlcohol WHERE a_winetypename = \"" + style + "\" AND a_typekey = w_typekey GROUP BY w_name;")
        
        db_connection.commit()
        result = db_cursor.fetchall()
        
        for row in result:
            print(row)
        drinkToFind = raw_input("If you would like to find locations where you can find a drink, please type in the drink name \n\n ")
        db_cursor.execute("SELECT l_name, l_address, l_phonenumber FROM location, foundat WHERE l_locationkey = f_locationkey AND f_winename LIKE '" + drinkToFind + "%';")
        db_connection.commit()
        result = db_cursor.fetchall()
        print("############# Locations ###############")
        for row in result:
            print(row)
        
    
    
    #db_cursor.execute("SELECT w_name FROM warehouse WHERE w_capacity <" + brewOrBlend + ";")
#db_connection.commit()

query2()
#input_data()
#db_cursor.execute(input1)

#result = db_cursor.fetchall()

#print("returned is a: ", type(result))

#print("############# Result ###############")
#for row in result:
#    print(row)

db_cursor.close()
db_connection.close()
print("Closed")
