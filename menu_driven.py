#!usr/bin/python

import time           #library to check current date and time
import webbrowser     #library to open browser   
import os             #library for shutdown,logout,create folder,create file
import urllib.request #library for checking internet connectivity
x='''
     Press 1  : To check current Date and Time.
     Press 2  : To create a File.
     Press 3  : To create a Directory.
     Press 4  : To search something on Google.
     Press 5  : Logout your System.
     Press 6  : To Shutdown your Opearting System.
     Press 7  : To check internet connection on your PC.
     Press 8  : Exit.
'''
print(x)
choice=input("Give your choice in integer ") 

if choice=='1':
	print("Showing current Date and Time")
	print(time.ctime()) #function for current date and time
elif choice=='2':
	print("Creating a file")
	f1= open("file1.txt","w") #Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists
	f1= open("file2.txt","x") #Open a file for exclusive creation. If the file already exists, the operation fails
	f1= open("file3.txt","a") #Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
elif choice=='3':
	print("Creating a Directory")
	path='/home/adhoc/Desktop/python/new'#defining location for new folder
	os.makedirs(path, exist_ok=True)     #function to make directory 
elif choice=='4':
	print("Searching on Google")
	msg=input("Type to search")
	webbrowser.open_new_tab('https://www.google.com/search?q='+msg) #open by new tab with url
elif choice=='5':
	print("Logout Your System")
	os.system('gnome-session-quit') #logout the current account 
elif choice=='6':
	print("Shutting Down the Operating System")
	print("Close all the applications")
	time.sleep(2)
	os.system("poweroff") #shutdown the computer
elif choice=='7':
	print("To check internet connection")
	url="https://www.google.com" 
	urllib.request.urlopen(url) #checking connection with url
	status="connected"
	print (status)
else:
	print("Wrong Option")

