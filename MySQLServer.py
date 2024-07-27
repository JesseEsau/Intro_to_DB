import mysql.connector

try:
    #Connect to my server
    mydb = mysql.connector.connect(

    host="localhost",
    user="Jesse",
    password="superDev",
)

    mycursor = mydb.cursor()

    #Create database 'alx_book_store' if it doesn't exist already
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created succeefully!")
except mysql.connector.Error as error:
    print(f"Error: {error}")
finally:
    #Close cursor and connection to database
    if 'mycursor' in locals():
        mycursor.close()
    if 'mycursor' in locals():
        mydb.close()
