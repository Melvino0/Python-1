corrpass = "computers"
corruser = "melvin"

username= input("usernamne: ").lower()
password= input("password: ")

#username= username.lower()

if (username == corruser):
    print("correct user: " + corruser) 
    if (password == corrpass):
        print("correct password: " + corrpass)
    else:
        print("wrong username")
else:
    print("wrong username: " + username)