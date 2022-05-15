#Library import with error messages.
try:
    import mysql.connector
    print("MySQL Connector imported successfully.")
except:
    print("Failed to import MySQL Connector!")