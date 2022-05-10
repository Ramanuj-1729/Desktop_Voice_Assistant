from openpyxl import load_workbook
import os
from Functions.Speak import speak


def addEmail():
    try:
        speak("Enter receiver name: ")
        userName = input("Enter user name: ")
        speak("Enter receiver mail id: ")
        emailId = input("Enter email id: ")

        data = [userName, emailId]
        file_name = os.path.realpath(os.path.join(os.path.dirname(
            __file__), '..', '..', 'Database', 'EmailDB', 'emailDB.xlsx'))
        wb = load_workbook(file_name)
        page = wb.active

        page.append(data)

        wb.save(filename=file_name)
        speak("Data added successfully")

    except:
        speak("Sir please close the database file, I am unable to add the data")
