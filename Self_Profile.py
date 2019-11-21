#Fromatted with Comma Sepration - May convert to CSV if necessary 
import datetime
import time 

def loading():
    return time.sleep(2)

loading()
with open("initmsg.txt") as skynet: 
        print(skynet.read())
        loading()
usr_name = str(input("Please Enter Your Name:\n"))
current_time = str(datetime.datetime.now())
loading()
print("Welcome", usr_name)
loading() 
print("Opening log file")
comment = str(input("Enter Comment \n"))
with open("log.txt","a") as logging: 
    logging.write(usr_name + ","+ current_time + "," + comment + "\n")
print("User Name and time has been appended to the Log file")
loading()
print("quitting")
loading()