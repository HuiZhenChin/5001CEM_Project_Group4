import mysql.connector

# Connect to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="alpha_enterprise"
)

#connection
cursor = connection.cursor()


def insert_data():
    #input
    id = input("Enter id: ")
    name = input("Enter name: ")
    phoneNumber = input("Enter phone number: ")
    email = input("Enter email: ")
    dpt = input("Enter department: ")
    password = input("Enter password: ")

    #SQL query to insert data
    query = "INSERT INTO staff (staffID, staffName, phoneNumber, staffEmail, staffDepartment, staffPassword) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (id, name, phoneNumber, email, dpt, password)

    #execute the query
    cursor.execute(query, values)

    #commit the changes to the database
    connection.commit()

    #display
    print("Data inserted successfully.")


def edit_data():
    #show existing id in the table
    cursor.execute("SELECT DISTINCT staffID FROM staff")
    ids = cursor.fetchall()
    print("Existing IDs:")
    for id in ids:
        print(id[0])

    #input
    id = input("Enter ID to edit: ")
    new_name = input("Enter new name: ")
    new_dpt = input("Enter new department: ")

    #SQL query to update data
    query = "UPDATE staff SET staffName = %s, staffDepartment = %s WHERE staffID = %s"
    values = (new_name, new_dpt, id)

    #execute the query
    cursor.execute(query, values)

    #commit the changes to the database
    connection.commit()

    print("Data updated successfully.")


def remove_data():
    cursor.execute("SELECT DISTINCT staffID FROM staff")
    ids = cursor.fetchall()
    print("Existing IDs:")
    for id in ids:
        print(id[0])

    #input
    id = input("Enter ID of the record to remove: ")

    #SQL query to delete data
    query = "DELETE FROM staff WHERE staffID = %s"
    values = (id,)

    #execute the query
    cursor.execute(query, values)

    #commit the changes to the database
    connection.commit()

    print("Data removed successfully.")


#enter choice
while True:
    print("\n1. Insert data")
    print("2. Edit data")
    print("3. Remove data")
    print("4. Quit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        insert_data()
    elif choice == "2":
        edit_data()
    elif choice == "3":
        remove_data()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

#close the connection
cursor.close()
connection.close()
