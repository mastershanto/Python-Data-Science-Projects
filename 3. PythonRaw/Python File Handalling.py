                # """File Handaling"""

# file=open("txtPy.txt","r")

# print(file.read())
# print()
# print(file.readline())
# print(file.readlines()) # List

# print(file.readable())

# file1=open("txtPy.txt","w")
# file1.write("Name: Lokman Hakim Shawon")
# file1.close()
# file_r=open("txtPy.txt","r")
# print(file_r.read())
# file_r.close()
# print(file_r.read())


# file2=open("txtPy.txt","a")
# file2.write("Name:Abu Akkas,\n, Desi: Peotry \n")

# file2.close()

# file3=open("txtPy.txt","r")
# file3.seek(0,1)

# print(file3.read())

# file4=open("txtPy.txt","r+")
# print(file4.read())
# file4.seek(0,0)
# file4.write("Java  ")
# file4.seek(0,0)
# print(file4.read())

# import os
# os.remove("txtPy.txt")

# import os
# file6=open("masterPy.txt","x")
# file6.close()

# file5=open("masterPy.txt","r+")

# file5.write("My name is Sheikh Ajijul Hoqeu (Shanto)")
# print(file5.read())

# print(file5.getcwd())


# import os
# os.mkdir("Py File Handaling Codes")
# os.chdir("I:\Python Data Science\BesicPython")
# os.chdir("Py File Handaling Codes")

# open("PyFH.txt","x")
# print(os.getcwd())
# FL1=open("PyFH.txt","r+")
# print(FL1.read())
# FL1.write("Ajijul Hoque Shanto, Roll: 856503")
# print(FL1.read())
# open("FH.xlsx","x")
# a=os.listdir(os.getcwd())
# for i in a:
#     print(i)

# import os
# os.rename("PyFH.txt","Py.txt")
# open("PyHand.txt","x")
# print(os.listdir(os.getcwd()))
# os.remove("Py.txt")
# print(os.getcwd())
# os.chdir("I:\Python Data Science\BesicPython")
# print(os.getcwd())
# os.rmdir("Py File Handaling Codes")
# print(os.listdir(os.getcwd()))
# import pickle

# open("binary.bin","x")
# file=open("binary.bin","wb")
# Data=["shato",1,3,"Shawon"]
# pickle.dupm(Data,file)
# file.close()
# import pickle
# file=open("binary.bin","rb")
# Data = pickle.load(file)
# for i in Data:
#     print(i)
# file.close()

import os,pickle
print(os.listdir(os.getcwd()))

# File=open("binary.bin","wb")

# Data=["shato",1,3,"Shawon",2]

# pickle.dump(Data,File)

# File.Close()

File=open("binary.bin","rb")

Data=pickle.load(File)
print(Data)


