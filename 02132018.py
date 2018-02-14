print( "Hello")
password=""
attempt=0
flag=0
while(attempt!=3):
    password = input("Enter Password ")
    if(password=="1234"):
        flag=1
        break
    else:
        attempt=attempt+1
        if(attempt==3):
            print("You are blocked for a while")
            exit()



user = input('Type your score ')
if user.isdigit():
    user1=int(user)
    if (user1 >=90):
        if (user1 > 100):
            print("Try again")
        else:
            print ("A")   
    elif (user1 >=80):
        print ("B")
    elif (user1 >=70):
        print ("C")
    elif (user1 >=60):
        print ("D")
    else:
        if (user1 <0):
            print("Negative impossible")
        else:
            print ("F")
else:
    print("INTEGER ONLY")


    
    
    
  


