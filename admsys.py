import mysql.connector
import time

class AdmSys:
    #constructor
    def __init__(self,server,user,pwd,db) -> None:
        self.server = server
        self.user = user
        self.pwd = pwd
        self.db = db
        self.con = mysql.connector.connect(host = server, username = user, password = pwd, database = db)
        
    #Wait for user input to get outta the function
    def mainmenu(self):
        goto_menu = input("Press ENTER to return to main menu.")
        print()
    
    #enroll function -- for inserting student details in the database   
    def enroll(self):
        print("Student Details:")
        name = input("\tName: ")
        parentage = input("\tParentage: ")
        gender = input("\tGender: ")
        class1 = input("\tClass: ")
        address = input("\tAddress: ")
        contact = input("\tContact: ")
        print(f"\nHere are the details you entered:\n1. Name: {name}\n2. Parentage: {parentage}\n3. Gender: {gender}\n4. Class: {class1}\n5. Address: {address}\n6. Contact: {contact}")
        print()
        while True:
            update = input("If you wanna correct any of the above details, enter the corresponding number or Enter 0 to submit: ")
            try:
                update = int(update)
                if update == 1:
                    name = input("Enter correct name: ")
                elif update == 2:
                    parentage = input("Enter correct parentage: ")
                elif update == 3:
                    gender = input("Enter correct gender: ")
                elif update == 4:
                    class1 = input("Enter correct class: ")
                elif update == 5:
                    address = input("Enter correct address: ")
                elif update == 6:
                    contact = input("Enter correct contact: ")
                elif update == 0:
                    try:
                        c = self.con.cursor()
                        query = f"INSERT INTO student_details(StudentName, Parentage, Gender, Class, Address, Contact) VALUES('{name}','{parentage}','{gender}','{class1}','{address}','{contact}');"
                        c.execute(query)
                        self.con.commit()
                        c.close()
                        print("\nSubmitted Successfully!\n")
                        self.mainmenu()
                        break
                    except:
                        print("\nOops! An error occured! Submission Unsuccessful!\n")
                        break
                else:
                    print("\nOops! You entered an invalid number. Submission Unsuccessful!\n")
                    self.mainmenu()
                    break
            except:
                print("\nOops! You entered an invalid number. Submission Unsuccessful!\n")
                self.mainmenu()
                break

    #view fuction -- for viewing student records from the database
    def view(self):
        c = self.con.cursor()
        query1 = "DESCRIBE student_details;"
        c.execute(query1)
        print(">>>STUDENT RECORD<<<")
        print("NOTE: Each row has the following format:")
        for i in c:
            print(i[0],end=" ")
        print()
        query2 = "select * from student_details;"
        c.execute(query2)
        for i in c:
            print(i)
        print()
        self.con.commit()
        c.close()
        self.mainmenu()

    #delete function -- for deleting records from the database
    def delete(self):
        try:
            id = int(input("Enter Student ID:"))
            c = self.con.cursor()
            query = f"select * from student_details where StudentID={id};"
            c.execute(query)
            found = list()
            for i in c:
                print(i)
                found.append(i)
            if len(found) != 1:
                print("Student Record Not Found!")
                self.mainmenu()
            elif len(found) == 1:
                delete_data = input(f"Would you like to delete data for this StudentID {id}(Y/N): ")
                query2 = f"delete from student_details where StudentID={id};"
                if delete_data.upper() == "Y":
                    c.execute(query2)
                    self.con.commit()
                    c.close()
                    print("Successfully Deleted!")
                    self.mainmenu()
                elif delete_data.upper() == "N":
                    print(f"Details of Student ID {id} not deleted.")
                    self.mainmenu()
                else:
                    print("Invalid Value!")
                    self.mainmenu()
        except:
                print("Oops! You entered an invalid value.")
                self.mainmenu()

    #update function -- for updating records in the database
    def update(self):
        try:
            id = int(input("Enter Student ID:"))
            c = self.con.cursor()
            query1 = f"select * from student_details where StudentID={id};"
            c.execute(query1)
            found = list()
            for i in c:
                print(f"Here are the details of Student ID {id}:\n\t1. Name: {i[1]}\n\t2. Parentage: {i[2]}\n\t3. Gender: {i[3]}\n\t4. Class: {i[4]}\n\t5. Address: {i[5]}\n\t6. Contact: {i[6]}")
                found.append(i)
            c.close()
            if len(found) != 1:
                print("Student Record Not Found!")
                self.mainmenu()
            elif len(found) == 1:
                while True:
                    update = input("If you wanna update only a particular field, enter the corresponding number or Enter 0 to update all.")
                    try:
                        update = int(update)
                    except:
                        print("\nOops! You entered an invalid value. Couldn't Update. Please TRY AGAIN!\n")
                        self.mainmenu()
                        break
                    try:
                        if update == 1:
                            name = input("Enter correct name: ")
                            c = self.con.cursor()
                            update_query = f"update student_details set StudentName='{name}' where StudentID={id};"
                            c.execute(update_query)
                            self.con.commit()
                            c.close()
                            print("Updated Successfully!")
                            self.mainmenu()
                            break
                        elif update == 2:
                            parentage = input("Enter correct parentage: ")
                            c = self.con.cursor()
                            update_query = f"update student_details set Parentage='{parentage}' where StudentID={id};"
                            c.execute(update_query)
                            self.con.commit()
                            c.close()
                            print("Updated Successfully!")
                            self.mainmenu()
                            break
                        elif update == 3:
                            gender = input("Enter correct gender: ")
                            c = self.con.cursor()
                            update_query = f"update student_details set Gender='{gender}' where StudentID={id};"
                            c.execute(update_query)
                            self.con.commit()
                            c.close()
                            print("Updated Successfully!")
                            self.mainmenu()
                            break
                        elif update == 4:
                            class1 = input("Enter correct class: ")
                            c = self.con.cursor()
                            update_query = f"update student_details set Class='{class1}' where StudentID={id};"
                            c.execute(update_query)
                            self.con.commit()
                            c.close()
                            print("Updated Successfully!")
                            self.mainmenu()
                            break
                        elif update == 5:
                            address = input("Enter correct address: ")
                            c = self.con.cursor()
                            update_query = f"update student_details set Address='{address}' where StudentID={id};"
                            c.execute(update_query)
                            self.con.commit()
                            c.close()
                            print("Updated Successfully!")
                            self.mainmenu()
                            break
                        elif update == 6:
                            contact = input("Enter correct contact: ")
                            c = self.con.cursor()
                            update_query = f"update student_details set Contact='{contact}' where StudentID={id};"
                            c.execute(update_query)
                            self.con.commit()
                            c.close()
                            print("Updated Successfully!")
                            self.mainmenu()
                            break
                        elif update == 0:
                            print(f"Enter updated details for Student Id {id}:")
                            name = input("\tName: ")
                            parentage = input("\tParentage: ")
                            gender = input("\tGender: ")
                            class1 = input("\tClass: ")
                            address = input("\tAddress: ")
                            contact = input("\tContact: ")
                            c = self.con.cursor()
                            update_query = f"update student_details set StudentName='{name}',Parentage='{parentage}',Gender='{gender}',Class='{class1}',Address='{address}',Contact='{contact}' where StudentID={id};"
                            c.execute(update_query)
                            self.con.commit()
                            c.close()
                            print("Updated Successfully!")
                            self.mainmenu()
                            break
                        else:
                            print("\nPlease! Enter a valid number.\n")
                            continue
                    except:
                        print("\nOops! An error occured! Couldn't Update!\n")
                        self.mainmenu()
                        break
        except:
                print("Oops! You entered an invalid value.")
                self.mainmenu()

    #for closing connection
    def close_con(self):
        self.con.close()

    #for saving the current database records in a text file
    def save(self):
        try:
            with open("Student Record.txt", "w") as fhand:
                fhand.write("STUDENT RECORD\n\nNOTE: Each row has the following format:\nID, Name, Parentage, Gender, Class, Address, Contact\n\n")
                c = self.con.cursor()
                query = "select * from student_details;"
                c.execute(query)
                for i in c:
                    fhand.write(f"{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}, {i[6]}\n")
                self.con.commit()
                c.close()
                print("Student record saved in a text file successfully!")
                self.mainmenu()
        except:
            print("An unknown error occurred. Please TRY AGAIN!")
            self.mainmenu()

#MAIN
heading = "====== Admission System 1.0 ======"
for i in heading:
    print(i, end="", flush=True)
    time.sleep(0.05)
time.sleep(1)
print()
print("USER LOGIN")
username = input("\tEnter username: ")
password = input("\tEnter password: ")
print("Please Wait! Connecting to DATABASE", end="")
for i in "...":
    print(i,end="",flush=True)
    time.sleep(0.5)
time.sleep(0.5)
print()
try:
    AdmissionSystem = AdmSys("localhost", username , password , "records")
    print("Successfully connected!")
    print()
    for i in f"User: {username}":
        print(i, end="", flush=True)
        time.sleep(0.05)
    print()
    time.sleep(0.5)
    while True:
        print("="*10 + " E-System " + "="*10)
        print("1. Enroll\n2. View Records\n3. Delete Records\n4. Update Records\n5. Save Records\n6. Exit Program")
        print("="*30)
        print()
        choice = input("Enter your choice: ")
        print()
        try:
            choice = int(choice)
            if choice == 1:
                AdmissionSystem.enroll()
            elif choice == 2:
                AdmissionSystem.view()
            elif choice == 3:
                AdmissionSystem.delete()
            elif choice == 4:
                AdmissionSystem.update()
            elif choice == 5:
                AdmissionSystem.save()
            elif choice == 6:
                AdmissionSystem.close_con()
                break

        except:
            print("Please! Enter a valid choice.")
            continue
    for i in "Thanks for using this program :)\nHave a nice day :)":
        print(i, end="", flush=True)
        time.sleep(0.05)
    print()
    close = input()
except:
    print("Oops! Can't connect to database!\nPlease check the login credentials!")
    close = input()
    exit()