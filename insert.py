import bcrypt
import base64
import mysql.connector

# Connect to the MySQL database
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test"
    )
    
    cursor = connection.cursor()
    path = "C:/Users/Jolyn Peh/Documents/pic2.jpg"
    image = open(path, 'rb').read()
    image_read = base64.b64encode(image)

    #not storing
    pwd = 'STAFF6'
    bytePwd = pwd.encode('utf-8')

    #salt
    salt = bcrypt.gensalt()

    #salted password
    password = bcrypt.hashpw(bytePwd,salt)

    query = "INSERT INTO staff (ID, NAME, PHONE, EMAIL, DEPARTMENT, PROFILE_PIC, PASSWORD, SALT) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"# 
    values = ('S183', 'TEOW JIA SHIUAN', '012-5782505', 'TEOW@ALPHA.STAFF.COM', 'IT DEPARTMENT', image_read, password, salt)
    
    cursor.execute(query, values)

    connection.commit()

except mysql.connector.Error as error:
    print("Failed to connect: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()