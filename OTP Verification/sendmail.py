import os,math
import random,sys
import smtplib
mailid=sys.argv[1]
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
msg='Your OTP Verification for app is '+OTP+' Note..  Please enter otp within 2 minutes and 3 attempts, otherwise it becomes invalid'
file2=open("otp.txt","w")
file2.write(OTP)
file2.close()
# &&&&&&&&&&&&- Your mail id. SENDING OTP FROM mail id
# ************- Your app password. If you do not know how to generate app password for your mail please google.
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("&&&&&&&&&&", "*********")
print(msg)
s.sendmail('&&&&&&&&&&&',mailid,msg)

os.system('python second.py')