"""
(C) NAIRDC 2022
Author(s): Samah Fujo
who are you?
Developer for this project
Created:
27/mm/yyyy
Last Update:
dd/mm/yyyy
By:
who are you?
Version:
1.0
...
File summary

This file will be responsible to encrypt python code by providing file path to be encrypted
"""
import marshal
import os

file_name = input("Enter file name with extension ==> :")
save_path = r"C:\nao-payroll-deployment-dock\NAO-Payroll\application"
completeName = os.path.join(save_path, file_name)
open_read = open(completeName).read()
compel = compile(open_read,"","exec")
dump = marshal.dumps(compel)
# start = open(save_path+"Uncode-"+file_name,"w")
start = open(completeName,"w")
start.write("import marshal\n")
start.write("exec(marshal.loads("+ repr(dump)+"))")
start.close()
print("{+} Encryption has been d`one successfully")



# Steps to share in get hub
# 1- VCS ==> Create git Repository
# 2- Git ==> Share Project on Github
