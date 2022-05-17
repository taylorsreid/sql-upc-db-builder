#default ansi code: \u001b[0m
#red ansi code: \u001b[31m

#Library import with error messages.
try:
    import mysql.connector
    print("MySQL Connector imported successfully...")
except:
    print("\n\t\u001b[31mFailed to import MySQL Connector!  You must run")
    print("\t\t\u001b[0mpip install mysql-connector-python")
    print("\t\u001b[31min command prompt or terminal to use this application.\n")

#opens the file with your credentials
#YOU MUST CREATE YOUR usrinfo.txt CREDENTIALS FILE FOR THIS PROGRAM TO WORK!
try:
    with open("usrinfo.txt", "r") as usrinfo:
        credentials = usrinfo.readlines()
except:
    print("No credentials file found or was unable to pull credentials.  Please see readme file.")

#connects to the MySQL database with the credentials specified in your usrinfo.txt file
#AGAIN -- YOU MUST CREATE YOUR usrinfo.txt CREDENTIALS FILE EXACTLY AS THE README SPECIFIES FOR THIS PROGRAM TO WORK!
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
    print(f"Successfully connected to MySQL database...\n")

#if there's a connection error
#AGAIN AGAIN -- YOU MUST CREATE YOUR usrinfo.txt CREDENTIALS FILE EXACTLY AS THE README SPECIFIES FOR THIS PROGRAM TO WORK!
except Exception as e:
    print("\n\t\u001b[31mError connecting to MySQL!  MySQL gave the following error:")
    print(f"\t\t{e}")
    print("\tPlease check that your connection credentials are correct and see the readme file!\n")
    exit()

#Ok now that we're done connecting and everything, here's where the fun actually begins.
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
            print("-"*80)
        except:
            print("\u001b[31mHmmmm something wasn't right about that input and MySQL didn't accept it.")
            print("MySQL does not accept duplicates.")
            print("You must have your database and credentials set up according to the readme, or modify the source code to match your database format.")
            print("You should also check your MySQL configuration.")
            print("Starting over...")
        finally:
            entry()
    else:
        print("\u001b[0mSorry about that, let's start over.")
        entry()
#starts the program
entry()