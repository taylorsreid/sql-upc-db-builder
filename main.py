#Library import with error messages.

#default ansi code: \u001b[0m
#red ansi code: \u001b[31m

try:
    import mysql.connector
    print("MySQL Connector imported successfully...")
except:
    print("\n\u001b[31mFailed to import MySQL Connector!  You must run")
    print("\t\u001b[0mpip install mysql-connector-python")
    print("\u001b[31min command prompt or terminal to use this application.\n")

try:
    with open("usrinfo.txt", "r") as usrinfo:
        credentials = usrinfo.readlines()
except:
    print("No credentials file found or was unable to pull credentials.  Please see readme file.")

try:
    #Locations & Credentials
    mydb = mysql.connector.connect(
        host = credentials[0].strip(),
        user = credentials[1].strip(),
        password = credentials[2].strip(),
        database = credentials[3].strip()
    )

    #cursor object declaration
    mycursor = mydb.cursor()
    print(f"\u001b[0mSuccessfully connected to MySQL database...\n")

    #BEGIN TEST CODE
    '''
    print("\nList of databases:")
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(f"\t {x}")
    print()
    '''
    #END TEST CODE

except:
    print("\u001b[31mError connecting to MySQL!  Please check your connection credentials and try again!")

#Ok now that we're done connecting and everything, here's where the fun actually begins.
#masterControlBool = True
def entry():
    sql = "INSERT INTO items (upc, name, price) VALUES (%s, %s, %s)"
    upc = input("\u001b[0mPlease input the UPC:  ")
    name = input(f"Please enter a name for {upc}:  ")
    price = input(f"Please input a price for {upc} {name}:  $")
    yesOrNo = input(f"\nDoes this look correct? \n\tUPC:  {upc} \n\tName:  {name} \n\tPrice:  ${price} \nEnter y if so to commit:  ")

    if yesOrNo.lower() == "y":
        val = (upc, name, price)
        try:
            mycursor.execute(sql, val)
            mydb.commit()
            print("Committed to table.")
        except:
            print("\u001b[31mHmmmm something wasn't right about that input and MySQL didn't accept it.  Let's start over.")
        finally:
            entry()
    else:
        print("\u001b[0mSorry about that, let's start over.")
        entry()
entry()