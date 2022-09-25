import tkinter
from tkinter import ttk
import random
import array
import mysql.connector

mydatabase = mysql.connector.connect(
    host,  ## Your host and user and password and create a database known as logins and then run the program
    user,
    password,
    auth_plugin= 'mysql_native_password',
    database='logins')

print("Connection established")
mycursor = mydatabase.cursor()


m = tkinter.Tk()
m.geometry("500x600")
m.title("Password Generator")


Login_label = tkinter.Label(m, text = 'LOGIN', font=('calibre',25, 'bold'))

name_label = tkinter.Label(m, text = 'Username', font=('calibre',13, 'bold'))
name_entry = ttk.Entry(m, font=('calibre',13,'normal'))

passw_label = tkinter.Label(m, text = 'Password', font = ('calibre',13,'bold'))
passw_entry=ttk.Entry(m,  font = ('calibre',13,'normal'), show = '*')


def Submit():
    sql = "SELECT * FROM customers WHERE name = %s"
    adr = (name_entry.get(), )

    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    userspasswordfinally = passw_entry.get()
    for x in myresult:

        originalpassword = x[1]
        if userspasswordfinally == originalpassword:
            AfterLogin = tkinter.Tk()
            AfterLogin.geometry("500x600")
            AfterLogin.title("Welcome Back !!")

            def GeneratePassword():
                MAX_LEN = 12
                DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                                     'z']

                UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                                     'Z']

                SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                           '*', '(', ')', '<']

                # combines all the character arrays above to form one array
                COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

                # randomly select at least one character from each character set above
                rand_digit = random.choice(DIGITS)
                rand_upper = random.choice(UPCASE_CHARACTERS)
                rand_lower = random.choice(LOCASE_CHARACTERS)
                rand_symbol = random.choice(SYMBOLS)

                temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

                for x in range(MAX_LEN - 4):
                    temp_pass = temp_pass + random.choice(COMBINED_LIST)


                    temp_pass_list = array.array('u', temp_pass)
                    random.shuffle(temp_pass_list)
                password = ""
                for x in temp_pass_list:
                    password = password+x

                print(password)
                Generated_P_L = tkinter.Label(AfterLogin, text = "Your generated password is :"+ password ,font = ('calibre',13,'bold'))
                Generated_P_L.place(x = 20 , y= 100)

                def savingpassword():
                    db2 = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    password ="soham0421",
                    auth_plugin = "mysql_native_password",
                    database = name_entry.get()
                    )
                    print("user connected")

                    pass_for = tkinter.Label(AfterLogin, text = 'Key For:', font=('calibre',13, 'bold'))
                    passwordn = ttk.Entry(AfterLogin, font=('calibre',13,'normal'))

                    pass_for.place(x=50, y = 250)
                    passwordn.place(x=200, y =250)


                    def saveitplease():
                        mydbcursor2 = db2.cursor()
                        sql = "INSERT INTO c_passwords (passwordfor, password) VALUES (%s, %s)"
                        val = (passwordn.get(),password)
                        print("Saved password for "+ passwordn.get()+ " password : "+password)

                    SS_P_Btn = tkinter.Button(AfterLogin, text = 'Save Password',command = saveitplease, height= 2)
                    SS_P_Btn.place(x = 150, y = 370)


                S_P_Btn = tkinter.Button(AfterLogin, text = 'Save Password',command = savingpassword, height= 2)
                S_P_Btn.place(x = 150, y = 150)










            G_P_Btn = tkinter.Button(AfterLogin, text = 'Generate New Password',command = GeneratePassword, height= 2)
            G_P_Btn.place(x = 150, y = 20)








def signup():
    upon = False
    signuppage = tkinter.Tk()
    signuppage.geometry("500x600")
    signuppage.title("Password Generator")
    Signup_label = tkinter.Label(signuppage, text = 'SIGN UP', font=('calibre',25, 'bold'))


    S_name_label = tkinter.Label(signuppage, text = 'Username', font=('calibre',13, 'bold'))
    S_name_entry = ttk.Entry(signuppage, font=('calibre',13,'normal'))


    S_passw_label = tkinter.Label(signuppage, text = 'Password', font = ('calibre',13,'bold'))
    S_passw_entry=ttk.Entry(signuppage, font = ('calibre',13,'normal'), show = '*')


    Signup_label.place(x=175, y =20)
    S_name_label.place(x= 70,y = 100)
    S_name_entry.place(x= 225, y = 100)

    S_passw_label.place(x=70,y = 200)
    S_passw_entry.place(x=225, y = 200)



    def S_signup():
        usersnamefinally = S_name_entry.get()
        userspasswordfinally = S_passw_entry.get()
        usersDatabase = mysql.connector.connect(
        host='localhost',
        user = 'root',
        password= 'soham0421',
        auth_plugin= 'mysql_native_password')

        usersCursor = usersDatabase.cursor()
        sql2 = "SHOW DATABASES"
        usersCursor.execute(sql2)
        lstrequired = usersCursor.fetchall()
        print(lstrequired)
        N = "(bytearray("+str(bytes(usersnamefinally,"UTF-8"))+"),)"
        if str(N) in str(lstrequired):
            print("Username taken already. ")
            upon = True
            if upon == True:
                U_sername_present = tkinter.Label(signuppage, text = 'Username Already Taken', font=('calibre',13, 'bold'))
                U_sername_present.place(x=70,y = 150)
        else :
            sql = "CREATE DATABASE "+ usersnamefinally
            usersCursor.execute(sql)
            D_C_S = tkinter.Label(signuppage, text = 'User Added Successfully, Please Close the App', font=('calibre',13, 'bold'))
            D_C_S.place(x= 80, y= 450)

            sql = "INSERT INTO customers (name, password) VALUES (%s, %s)"
            val = (usersnamefinally,userspasswordfinally)
            mycursor.execute(sql, val)

            sqlw = "use "+ usersnamefinally
            mycursor.execute(sqlw)

            mycursor.execute("CREATE TABLE c_passwords (id INT AUTO_INCREMENT PRIMARY KEY, passwordfor VARCHAR(255), password VARCHAR(255))")

            print("Table created successfully")
            fsql = "SHOW TABLES"
            mycursor.execute(fsql)
            for x in mycursor :
                print(x)

            mydatabase.commit()





    S_signup_btn=tkinter.Button(signuppage,text = 'Signup', command = S_signup, height= 2, width=20)

    S_signup_btn.place(x =150, y = 400)




    signuppage.mainloop()

sub_btn=tkinter.Button(m,text = 'Submit', command = Submit, height= 2, width=20)
signup_btn=tkinter.Button(m,text = 'Signup', command = signup, height= 2, width=20)

Login_label.place(x=175, y = 20)
name_label.place(x= 70,y = 100)
name_entry.place(x= 225, y = 100)

passw_label.place(x=70,y = 200)
passw_entry.place(x=225, y = 200)

sub_btn.place(x= 150, y = 300)
signup_btn.place(x =150, y = 400)


m.mainloop()
