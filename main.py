#Library import with error messages.
try:
    import mysql.connector
    print("MySQL Connector imported successfully...")
except:
    print("Failed to import MySQL Connector!  You must run")
    print("\u001b[31m pip install mysql-connector-python")
    print("\u001b[0m in command prompt / terminal to use this application.")

#Locations & Credentials
mydb = mysql.connector.connect(
    host = "", #STORE IN A SEPARATE FILE THAT IS GITIGNORED
    user = "", #STORE IN A SEPARATE FILE THAT IS GITIGNORED
    password = "" #STORE IN A SEPARATE FILE THAT IS GITIGNORED
)

#TEST CODE
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)