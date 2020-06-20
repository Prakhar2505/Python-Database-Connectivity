#Install and import all the imp libraries i.e. Tkinter and sqlite3
import tkinter as tk
import sqlite3

#opens a connection to the SQLite database file
connection = sqlite3.connect('student.db')
print('Database opened successfully')

#Decide the parameters for your database
TABLE_NAME = "student_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

#creating table in the database (syntax same as sql)
connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY " + " AUTOINCREMENT, " + STUDENT_NAME + " TEXT, "+
                   STUDENT_COLLEGE + " TEXT, " + STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER );")

#creating gui window
mainWindow = tk.Tk()

#giving title to window
mainWindow.title('Student Database')

#giving 1 label and then asking its value in the namefield and so on for other parameters
#This Label will prompt user to input name
heading_label1 = tk.Label(mainWindow, text="ENTER YOUR NAME")
heading_label1.pack()

#Here user will input the name
name_field1 = tk.Entry(mainWindow)
name_field1.pack()

heading_label2 = tk.Label(mainWindow, text="ENTER YOUR COLLEGE")
heading_label2.pack()

name_field2 = tk.Entry(mainWindow)
name_field2.pack()


heading_label3 = tk.Label(mainWindow, text="ENTER YOUR ADDRESS")
heading_label3.pack()

name_field3 = tk.Entry(mainWindow)
name_field3.pack()

heading_label4 = tk.Label(mainWindow, text="ENTER YOUR PHONE NUMBER")
heading_label4.pack()

name_field4 = tk.Entry(mainWindow)
name_field4.pack()

#Appending input values into the database
#Putting in a try and catch block to deal with null values and fowl inputs
def takeValueInput():
    try:
        #Storing the input values into a corresponding variable
        name = name_field1.get()
        college = name_field2.get()
        address = name_field3.get()
        phone = name_field4.get()
        phone = float(phone)

        #Appending variable values into database , syntax same as in sql
        connection.execute(
            "INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " + STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " + STUDENT_PHONE + ") VALUES(?, ?, ?, ?); ",
            (name, college, address, phone))

        #saving changes to the database
        connection.commit()

        #After input clearing the input fields
        name_field1.delete(first=0, last=22)
        name_field2.delete(first=0, last=22)
        name_field3.delete(first=0, last=22)
        name_field4.delete(first=0, last=22)
        print('Input Successfull')

    #Incase user tries to save without entering any value in the field
    except ValueError:
        print("----------Enter Correct Values-------------")

    #Incase any field is left blank
    except:
        print("--------Dont leave any column blank")
    #You can create more such cases

#Displaying values from the database on the console
def show_database():
    #Extracting all the data from the table
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")

    #processing row by row
    for row in cursor:
        print("\nStudent id is: ", row[0])
        print("Student name is ", row[1])
        print("Student college is", row[2])
        print("Student College address is", row[3])
        print("Student phone is", row[4])

#A button to save the data using the func takeValueInput()
button = tk.Button(mainWindow, text="SAVE ", command=lambda:takeValueInput())
button.pack()

#A button to display data using the func show_database()
button = tk.Button(mainWindow, text="SHOW ", command=lambda:show_database())
button.pack()

#To keep the program active as long as the window is not closed
mainWindow.mainloop()

#Closing connection to the database
connection.close()