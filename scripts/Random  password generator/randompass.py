import random
import string
#User input password length
passlen=int(input("Enter the length of password:"))
password=''
#In the following line it joins the choice from the random module created in machine and it displays the password according to the size
password= ''.join([random.choice(string.ascii_letters + string.digits+ '!@#$%^&*' ) for n in range(passlen)])
#Here a random password is created
print("Your password is:-",str(password))