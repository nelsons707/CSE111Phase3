import os
import sqlite3   ## Include SQLite package
import random

################ Connect SQLite Database ################

db_connection = None # Define the connection parameter
db_name = "/Users/jasonrocha/Documents/CSE111/Project/project.db" # Specify the full path of Database file

try:
    db_connection = sqlite3.connect(db_name)
except sqlite3.Error as err: # If database connection failed this block of code  # handles the exception
    print(err)

if db_connection:
    print(db_connection) # Printing the connection object
    print("Successfully Established connection with SQLite3")
    print("\n\n")

################ Code ################

intoBrewery = False

intoWinery = False

intoBeer = False

intoWine = False


db_cursor = db_connection.cursor()


def input_data():
    if intoBrewery == True:
        br_name=raw_input("Enter Brewery Name: ")
        br_description=raw_input("Enter a Description: ")
        br_locationkey = random.randint(1,100)
        db_cursor.execute("INSERT INTO brewery(br_name, br_locationkey, br_description) VALUES(?,?,?)",(br_name, br_locationkey, br_description))
        db_connection.commit()
        restartProgram = raw_input("\nPress r to restart || Press e to exit \n> ")
        if restartProgram == "r":
            Menu()
        elif restartProgram == "e":
            quit()

    elif intoWinery == True:
        wi_name=raw_input("Enter Winery Name: ")
        wi_description=raw_input("Enter a Description: ")
        wi_locationkey = random.randint(1,100)
        db_cursor.execute("INSERT INTO Winery(wi_name, wi_locationkey, wi_description) VALUES(?,?,?,?,?,?)",(wi_name, wi_locationkey, wi_description))
        db_connection.commit()
        restartProgram = raw_input("\nPress r to restart || Press e to exit \n> ")
        if restartProgram == "r":
            Menu()
        elif restartProgram == "e":
            quit()

    elif intoWine == True:
        w_name=raw_input("Enter wine Name: ")
        w_ABV=float(raw_input("Enter the ABV: "))
        w_typekey=int(raw_input("Enter a key: "))
        w_year=int(raw_input("Enter the year it was made: "))
        w_description=raw_input("Enter a description: ")
        db_cursor.execute("INSERT INTO wine(w_name, w_ABV, w_typekey, w_year, w_description) VALUES(?,?,?,?,?)",(w_name, w_ABV, w_typekey, w_year, w_description))
        db_connection.commit()
        restartProgram = raw_input("\nPress r to restart || Press e to exit \n> ")
        if restartProgram == "r":
            Menu()
        elif restartProgram == "e":
            quit()

    elif intoBeer == True:
        b_name=raw_input("Enter beer Name: ")
        b_ABV=float(raw_input("Enter the ABV: "))
        b_typekey=int(raw_input("Enter a key: "))
        b_IBU=float(raw_input("Enter the IBU: "))
        b_description=raw_input("Enter a description: ")
        db_cursor.execute("INSERT INTO beer(b_name, b_ABV, b_typekey, b_IBU, b_description) VALUES(?,?,?,?,?)",(b_name, b_ABV, b_typekey, b_IBU, b_description))
        db_connection.commit()
        restartProgram = raw_input("\nPress r to restart || Press e to exit \n> ")
        if restartProgram == "r":
            Menu()
        elif restartProgram == "e":
            quit()


def query2():
    brewOrBlend=raw_input("What do you feel like drinking tonight? Enter beer or wine: ")
    
    if brewOrBlend == "beer" or brewOrBlend == "Beer":
        print("\n")
        style=raw_input("What style of beer would you like? \nEnter from the following: \nAle \nWheat Ale \nPilsner \nStout \nLager \n> ")
        print("\nBeers: ")
        db_cursor.execute("SELECT b_name FROM beer, TypesOfAlcohol WHERE a_beertypename = \"" + style + "\" AND a_typekey = b_typekey GROUP BY b_name;")
        
        db_connection.commit()
        result = db_cursor.fetchall()
        db_connection.commit()
        for row in result:
            print(row[0])
    
        print("\n")
        drinkToFind = raw_input("If you would like to find locations where you can find a drink, please type in the drink name: \n> ")
        db_cursor.execute("SELECT l_name, l_address, l_phonenumber FROM location, foundat WHERE l_locationkey = f_locationkey AND f_beername LIKE'" + drinkToFind + "%';")
        print("\n")
        db_connection.commit()
        result = db_cursor.fetchall()
        print("Location:")
        for row in result:
            print row[0], row[1], row[2]
        restartProgram = raw_input("\nPress r to restart || Press e to exit \n> ")
        if restartProgram == "r":
            Menu()
        elif restartProgram == "e":
            quit()

    elif brewOrBlend == "wine" or breworBlend == "Wine":
        print("\n")
        style = raw_input("What style of wine would you like? \nEnter from the following: \nPinot Noir \nSyrah \nCabernet Sauvigon \nRed Blend \nChardonnay \nZinfandel \nRose \n> ")
        print("\nWines: ")
        db_cursor.execute("Select w_name FROM wine, TypesOfAlcohol WHERE a_winetypename = \"" + style + "\" AND a_typekey = w_typekey GROUP BY w_name;")
        
        db_connection.commit()
        result = db_cursor.fetchall()
        
        for row in result:
            print(row[0])
        
        print("\n")
        drinkToFind = raw_input("If you would like to find locations where you can find a drink, please type in the drink name \n> ")
        db_cursor.execute("SELECT l_name, l_address, l_phonenumber FROM location, foundat WHERE l_locationkey = f_locationkey AND f_winename LIKE '" + drinkToFind + "%';")
        print("\n")
        db_connection.commit()
        result = db_cursor.fetchall()
        print("Location:")
        for row in result:
            print row[0], row[1], row[2]
        restartProgram = raw_input("\nPress r to restart || Press e to exit \n> ")
        if restartProgram == "r":
            Menu()
        elif restartProgram == "e":
            quit()


def Menu():
    intoBrewery = False
    intoBeer = False
    intoWinery = False
    intoWine = False
    
    addOrSearch=raw_input("Choose from the following commands: \nAdd \nSearch \n>")
    if addOrSearch == "Add" or addOrSearch == "add":
        addWhere=raw_input("\nWhich of the following tables would you like to insert to? \nBrewery \nWinery \nWine \nBeer\n>")
        if addWhere == "Winery" or addWhere == "winery":
            intoWinery = True
        elif addWhere == "Brewery" or addWhere == "brewery":
            intoBrewery = True
        elif addWhere == "Wine" or addWhere == "wine":
                intoWine = True
        elif addWhere == "Beer" or addWhere == "beer":
            intoBeer = True
        input_data()

    elif addOrSearch == "Search" or addOrSearch == "search":
        query2()


Menu()
#input_data()
#db_cursor.execute(input1)

#result = db_cursor.fetchall()

#print("returned is a: ", type(result))

#print("############# Result ###############")
#for row in result:
#    print(row)

db_cursor.close()
db_connection.close()
