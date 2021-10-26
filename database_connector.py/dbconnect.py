#imoprt the package
import MySQLdb

#enter the database details
db = MySQLdb.connect(host= input("> Input the your host adress here: "),    
                     user=input("> Input your username here: "),         
                     passwd=input("> Input your password here"),  
                     db=input("> Input the name of your Database here: "))    
#check if its connected
print("connection successful")
cur = db.cursor()

#open what you want
cur.execute(input("> Input the file you want to open in your Database"))

#print out the data
for row in cur.fetchall():
    print(row[0]) 