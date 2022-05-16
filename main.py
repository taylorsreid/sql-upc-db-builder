#Library import with error messages.
import getpass
try:
    import mysql.connector
    print("MySQL Connector imported successfully...")
except:
    print("Failed to import MySQL Connector!  You must run")
    print("\t\u001b[32m pip install mysql-connector-python")
    print("\u001b[0m in command prompt or terminal to use this application.")

#
try:
    #Locations & Credentials
    mydb = mysql.connector.connect(
        '''
        host = input("Host address:  "),
        user = input("Username:  "),
        password = getpass.getpass()
        '''

        host = "",
        user = "",
        password = ""
    )
    #cursor object declaration
    mycursor = mydb.cursor()
    print("Successfully connected to MySQL database...")

    #BEGIN TEST CODE
    print("\nList of databases:")
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(f"\t {x}")
    print()
    #END TEST CODE

except:
    print("Error connecting to MySQL database!  Please check your connection credentials and try again!")

