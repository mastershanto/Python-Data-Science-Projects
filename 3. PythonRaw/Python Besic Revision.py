
# # import turtle
# # colors = ["red","purple","blue","green", "orange","yellow"]
# # my_pen=turtle.Pen()
# # turtle.bgcolor("black")
# # for x in range(360)
# #     my_pen.pencolor(colors[x%6])
# #     my_pen.width(x/100+1)
# #     my_pen.forward(x)
# #     my_pen.left(59)




#               #Value Print & Separator Print

# # print("Shanto",58,"Rafiq","Shafiq",sep="-",end="\n\n")


#                 #New Line Print

# # print("mastershanto","Ajijul Hoque",end="\n\n")
# # print("Learn Something Everyday")

#                 # File & Flush
 
#           #Multiple arguments
#           # 1.Pass values as parameters

# # a="I"
# # b="Love"
# # c="You"
# # print("Hay",a,b,c) 

#          # 2.Use String formation 
#          #2.1 sequential formation pass value= ("{}")
# # a="I"
# # b="You"
# # c="Me"
# # print("{} Love {}".format(a,b)) 
# # print("{} Love {}".format(a,c)) 

#                 # 2.2Formating the Numbers= ("{1}{0}")
# # a="I"
# # b="You"
# # c="Me"
# # print("{1} Love {0}".format(a,b)) 
# # print("{1} Love {0}".format(a,c)) 

#                 #2.3Formatting with explicit names= ("{Name}")
# # a="I"
# # b="You"
# # c="Me"
# # print("{Name1} Love {Name2}".format(Name1=b,Name2=c))
# # print("{Name2} Love {Name1}".format(Name1=a,Name2=b))

#                #3.Pass Value as Tuple= ("%s"%())
# # a="I"
# # b="You"
# # c="Me"
# # print("%s Love %s "%(b,c))
# # print("Shanto, %s Love %s"%(a,b))
# # print("{} Love {}".format(b,c))
# # print("{Name2} Love {Name1}".format(Name1=b,Name2=c))
# # print("{Name1} Love {Name2}".format(Name1=b,Name2=c))


# # a="I"
# # b="You"
# # c="Me"
# # print("%s Love %s "%(b,c))
# # print("Shanto, %s Love %s"%(a,b))
# # print("{} Love {}".format(b,c))
# # print("{Name2} Love {Name1}".format(Name1=b,Name2=c))
# # print("{Name1} Love {Name2}".format(Name1=b,Name2=c))

#                           #Operators
# # Eight Kinds of Operators: Arithmetic, Assingment, Comparison, Logical,
# #Logical, identity, Membership, bitwise, Ternar

#                 # List of Arithmetic Operators: 
# # 1. Addition(+), 2. Subraction(-), 3. multiplication(*), 
# # 4. Division-Float(/), 5. Division-Float(//) 6. Modulus(%),
# # 7. Power(**)


# # a=10
# # b=2

# # print(a+b) #Addition+
# # print(a-b) #Substration-
# # print(a*b) #Multiplication*
# # print(a/b) #Divition1/
# # print(a//b) #Divition2//
# # print(a%b) #Modulus%
# # print(a**b) #Power**


#                    #Comparision/Reletional Operator
# # 1. Equal(==), 2. Not Equal(!=), 3. Greater than(>),
# # 4. Less then(<),  5. Greater then or Equal to(>=),
#  # 6. Less than or equal to(<=) 
        
# # a=10
# # b=10

# # print(a==b)  #Equal to==
# # print(a!=b) #Not Equal to!=
# # print(a>b) #Greater than>
# # print(a<b) #Less Than<
# # print(a>=b) #Greater than & Equal to>=
# # print(a<=b,"\n\n") #Less than & Equal to<=

# # a=12
# # b=10
# # print(a==b)
# # print(a!=b) 
# # print(a>b)
# # print(a<b)
# # print(a<=b)
# # print(a>=b)

#                     #Logical Operator
# # 1. AND, 2. OR, 3. NOT

# # a=10
# # b=5

# # print(a==10 and b==5) #AND
# # print(a==10 or b==6)  #OR
# # print(not b==5)       #NOT

#                   #Identity OPerator
#  # 1. is, 2. is not
 
# #  a=5
# #  b=5
# #  print(a is b)
# # print(a is not b)

#                  #Bitwise Operators
# # 1. Bitwise AND(&), 2. Bitwise OR (|), 3. Bitwise NOT (~), 
# # 4.Bitwise XOR(^), 5. Bitwise Right Shift (>>), 6. Bitwise LeftShift (<<).

# # a=10
# # b=12
# # print(a&b) #AND(&)
# # print(a|b) #OR(|)
# # print(~b)  #NOT(~)
# # print(a^b) #XOR(^)
# # print(b>>2)#Right Shift(>>)
# # print(b<<2) #Leftshift(<<)

# #                     #Assignment Operators
# # # 1. Assings Value(=), 2. Add Equal(+=), 3. Subtruction Equal(-=),
# # # 4.Multiply Equal(*=), 5. Division Equal(/=), 6. Floor Division Equal(//=),
# # # 7. Modulus Equal(%=), 8. Exponent Equal(**=)

# # a=10
# # a+=10 #a=a+10, Add Equal
# # print(a)
                    
# # a=10
# # a-=10 #a=a-10, Subtraction Equal
# # print(a)

# # a=10
# # a*=10 #a=a*10, Multiply Equal
# # print(a)

# # a=10
# # a/=10  #a=a/10, Division Equal
# # print(a)

# # a=10
# # a//=10 #a=a//10, Floor Division Equal
# # print(a)

# # a=10
# # a%=10 #a=a%10, Modulus Equal
# # print(a)

# # a=10
# # a**=10 #a=a**10, Eponent Equal
# # print(a)

# #  # 9. Bitwise AND Equal(&=), 10. Bitwise OR Equal(|=), 11. Bitwise XOR Equal(^), 
# #  # 12. Bitwise Rightshift Equal(>>=), 13. Bitwise Leftshift Equla (<<=)

# # a=30
# # b=13
# # a&=b #a=a&10
# # print(a)

# # a=30
# # b=13
# # a|=b #a=a|10
# # print(a)

# # a=30
# # b=13
# # a^=b #a=a^10
# # print(a)

# # a=30
# # b=13
# # a>>=2 #a=a>>2

# # print(a)


# # a=30
# # a<<=2 #a=a>>2

# # print(a)

#                                #Ternary Operators
 

#                        #Now Flow control/ Dicision Making 
# # 1. If, 2. else, 3. elif, 4. Nested if, 5. while loop, 6. for loop,
# # 7. continue, 8. pass, 9. break, All. Flowchart

#                              #Symble used in Flowchart: 
# # 1. start/stop, 2. input/output, 3. flowline, 4. processing, 5. decision

# # a="Cake"
# # if a=="Chocolate":
# #     print("Home work is done")
    
# # if a=="Soup":
# #     print("No Home works is here")

# # else:
# #     print("Home work is not done")


 
#                    #Nested If                     

# # a="Chocolate"
# # b="Cake"
 
# # if a=="Chocolate":
# #     print("Home Work is done.")
# # elif b=="cake":
# #     print("Home works is done_V2.")
# # else: 
# #     print("Home work is  not  finnised")
    
# # print("Ajijul Hoque Shanto")



#                 #While Loop
#                 #1. Infinite Loop
#                 #2. Nested Loop
#                 #3. Else Block
                
# # i=1
# # j=2

# # while i<=5:
# #     while j<=5:
# #         print("i= ",i," j=",j,sep=" ")
# #         j+=1
# #     i+=1
# #     j=1

#                 #Else Block
# # i=1
# # j=2
# # while i<=5:
# #     while j<=5:
# #         print("i=",i," j=",j,sep=" ")
# #         j+=1
# #     else:
# #         print("J is end")
# #     i+=1
# #     j=1


# # i=1
# # j=2
# # while i<=5                                 
# #     while j<=5:
# #         print("i=",i," j=",j,sep=" ")
# #         j+=1
# #     else:
# #         print("J is end")
# #     i+=1
# """ 
# Ans is: 
# i= 1  j= 2
# i= 1  j= 3
# i= 1  j= 4
# i= 1  j= 5
# J is end
# J is end
# J is end
# J is end
# J is end
# """

#                         #For Loop - range(Start,Iteam,Sep)

# # a="masterShanto"
# # for i in a:
# #     print(i)


# # for i in range(5):
# #     print(i)

# # for i in range(1,5):
# #     print(i)


# # for i in range(1,11,2):
# #     print(i)

# # for i in range(1,11,3):
# #     print(i)
    
#                             #Nested For Loop - else block
# # for i in range(1,6):
# #     for j in range(1,6):
# #         print(i,j)  


# # for i in range(1,6):
# #     for j in range(1,6):
# #         print("i=",i," j=",j, sep=" ")
# #     else: 
# #         print("J is end \n\n")
        
# # else:
# #         print("Loop is end")


#                 # use of "break, continue, pass" with while & for loops



# # for i in range(1,50):
# #     if i==11:
# #         break
# #     print("i=",i)
    
# # for i in range(1,50):
# #     if i==11:
# #         pass
# #     print("i=",i)
    
# # for i in range(1,6):
# #     if i==3:
# #         continue
# #     print("i=",i)

# # i=1
# # while i<=6:
# #     if i==3:
# #         break
# #     print("i=",i)
# #     i+=1


# # i=1
# # while i<=10:
# #     if i==3:
# #         continue  # it can't go to print fuction
# #     print("i=",i)
# #     i+=1

# # i=1
# # while i<=5:
# #     if i==3:
# #         pass
# #     print("i=",i)
# #     i+=1
    
     
#                         #### Data Types #####
# #1. None, 2. Boolean, 3. Number, 4. String, 5. List, 6. Tuples,
# # 7. Set, 8. Dictionary


#                              #None Type
# # a=10
# # a=None
# # print(a)                            

# # a=10
# # a=None

# # if a==None:
# #     print("A is None")
# # else:
# #     print("A is not None")
# # print(type(a))
    
# # a=10
# # a=None
# # a=5

# # if a==None:
# #     print("A is None")
# # else:
# #     print("A is not None")
# # print(type(a))
   

    
#                                 # Boolean Types (1. True, 2. False)
# # print(10<20)
# # print(type(10>20))


# # if 10<20:
# #     print("10 is Small")
# # else: print( "20 is big")

# # a=10<20
# # if a==True:
# #     print("10 is Small")
# # else: print( "20 is big")


#                               # Number Types (Int, Float, Complex)       
# # a=3
# # print(a, type(a))                              

# # b=3.534537883
# # print("{:.4f}".format(b),type(b))
# # print("{:.2f}".format(b))

# # c=10+12j
# # print(10+c)

# # print(10j+c)

# # print("{:.2f}".format(7.58384+c))
# # print("{:.2f}".format(7.58384j+c))
# # print("{:.2f}".format(7.58384j-c))
# # print(10j*c) # How to calculate , I have to realize next


# #                             # String
# # a='Now I am woring with "Python"'
# # print("\n",a,type(a),"\n")

# #                             #String - Multiline
# # a="""shanto is woring 
# #     with python.. todays
# #     nigh he will prectices it"""
# # print(a,"\n\n", type(a))


#                             #Positive Index, Negetive Index, length

# # e="masterShanto"
# # print(len(e)) 
# # print(e[5]) 
# # print(e[-7])   

#                             #Range/Slice, Change, Delete, Loop
# # h="masterShanto"                  
# # if "masterShanto"==h:
# #     print("matched")
# # else:
# #     print("Unmatched")


    
#                                     # Range/Slice

# # e="masterShanto"
# # f=e[:6]+" Ajijul_Hoque "+e[6:]
# # print(e[:10])
# # print(f)


#                                     #Length
# # e="masterShanto"

# # Length=0

# # for i in e:
# #    Length+=1
# #    print("Length",Length)
# # print()

# # print("Main Str Length= ",Length)                               

# # print(len(e))

# # f="""Sheikh
# #     Ajijul
# #     Hoque
# #     Shanto"""
    
# # print(len(f))

# # print("{0:*>50}".format(e))
    

#                                     # Membership (1. in, 2. not in)
                                    
# # e="masterShanto"                                

# # print("h" in e)
# # print("H" not in e)
                                    
#                                     # Concatination
                                    
# # e="masterShanto "                                    
# # f="Sheikh "
# # g="Ajijul "
# # h="Hoque "
# # i="Shanto "

# # print(e+f+g+h+i+" theMaster")

          
#                                     # Repetition
                                    
                                    
                                    



# # e="master "
# # f="Shanto"
# # g="Ajijul"
# # h="Hoque"

# # print(e*3)
# # print(e*10)


#                                 #Relation Operator
# # e="master "
# # f="Shanto"
# # g="Ajijul"
# # h="Hoque"

# # if "master " == e:
# #     print("\n Matched \n")
# # else:
# #     print("Not matched \n\n")


# # if "Shanto" >  "Shanto":
# #     print("Matched")
# # else:
# #     print("Not matched")


# #                                 #formate
                                
                                
                                
# #                                 #Method
# # # 1. Capitalize(), 2. Title(), 3. Upper(), 4. Lower(), 5. casefold(), 7. join(), 8. find()
# # # 9. rfind(), 10. Center(), 11. ljust(), 12. rjust(), 13.Strip(), 14. lstrip(), 15. rstip()
# # #16. splite(), 17. splitlines(), 18. swapcase(), 19. startwith(), 20. endwith()
# # #21. Count, 22. rsplit, 23. partition()





# # a="Doremon is my favourite Cartoon"

# # #1
# # print(a.capitalize())

# # #2
# # print(a.title())

# # #3
# # print(a.upper())

# # #4
# # print(a.lower())

# # #5
# # b="#@&*(()"
# # print(b.casefold()) 

# # #7
# # print("*".join(a[5:20]),"\n")                               
# # print(a.join('""'))
# # print(a.join('**'))
# # print(a.join('#'))
# # print(a.join('$$'))


# # #8
# # print(a.find("e")) #find means find from left
# # print(a.find("is"))
# # print(a.find("Cartoon"))

# # #9
# # print(a.rfind("is")) #find means find from right
# # print(a.rfind("e"))

# # #10

# # print(a.center(50,"*"))
# # print(a.center(50,"#"))
# # print(a.center(50,"$"))

# # #11 
# # print(a.ljust(50,"*"))

# # #12
# # print(a.rjust(50,"*"))
 
# # #21 Count
# # print(a.count("r"))
# # print(a.count("o"))

# # #13,14,15
# # c="ffffffffmy fevorite Cartoon is Doremon333333333"
# # print(c.strip("f 3"))
# # print(c.lstrip("f 3"))
# # print(c.rstrip("f 3"),"\n\n")


# # #16, 22
# # d=a.split()
# # print(a.split(),"\n", type(a.split()))
# # print(d[3])

# # print(a.split("o"))
# # print(a.split("my"))
# # print(a.split(" "))

# # print(a.split(" ",2))

# # print(a.rsplit(" ",2))


# # # 1. Capitalize(), 2. Title(), 3. Upper(), 4. Lower(), 5. casefold(), 7. join(), 8. find()
# # # 9. rfind(), 10. Center(), 11. ljust(), 12. rjust(), 13.Strip(), 14. lstrip(), 15. rstip()
# # #16. splite(), 17. splitlines(), 18. swapcase(), 19. startwith(), 20. endwith()
# # #21. Count, 22. rsplit, 23. partition(), 24. Zfill(), 25. replace()
# # # 26. islower()

# # #17
# # f="Doremon is my fevourit \ncartoon"
# # print(f.splitlines(True))
# # print(f.splitlines(False))

# # #18

# # print(a.partition("my"))
# # print(a.rpartition("my"))

# # #19
# # print(a.swapcase())

# # #20
# # print(a.endswith("my"))
# # print(a.endswith("n"))

# # #21
# # print(a.startswith("D"))

# # # 1. Capitalize(), 2. Title(), 3. Upper(), 4. Lower(), 5. casefold(), 7. join(), 8. find()
# # # 9. rfind(), 10. Center(), 11. ljust(), 12. rjust(), 13.Strip(), 14. lstrip(), 15. rstip()
# # #16. splite(), 17. splitlines(), 18. swapcase(), 19. startwith(), 20. endwith()
# # #21. Count, 22. rsplit, 23. partition(), 24. Zfill(), 25. replace()
# # # 26. islower(), 27. istitle(), 28. isupper()


# # #24
# # print(a.zfill(50))
# # print(a.rjust(50,"*"))

# # #25
# # print(a.replace("Doremon","My Wife"))

# # #26
# # print(a.islower())

# # #27
# # m="Master Shatno Sheikh Ajijul Hoque Shanto"
# # print(m.istitle())
# # s=m.casefold()
# # print(s)
# # print(s.islower())

# # # 1. Capitalize(), 2. Title(), 3. Upper(), 4. Lower(), 5. casefold(), 7. join(), 8. find()
# # # 9. rfind(), 10. Center(), 11. ljust(), 12. rjust(), 13.Strip(), 14. lstrip(), 15. rstip()
# # # 16. splite(), 17. splitlines(), 18. swapcase(), 19. startwith(), 20. endwith()
# # # 21. Count, 22. rsplit, 23. partition(), 24. Zfill(), 25. replace()
# # # 26. islower(), 27. istitle(), 28. isupper(), 29. isnumeric()
# # # 30. isdigit(), 31. isdecimal(), 32. isalpha(),33. isalnum

# # #28
# # t=s.upper()
# # print(t)
# # print(t.isupper())

# # #29
# # nm="25858"
# # print(nm.isnumeric())

# # #30
# # print(nm.isdigit())

# # #31
# # nm2="25858.5835"
# # print(nm2.isdecimal())

# # #32
# # print(nm2.isalpha())

# # # 1. Capitalize(), 2. Title(), 3. Upper(), 4. Lower(), 5. casefold(), 7. join(), 8. find()
# # # 9. rfind(), 10. Center(), 11. ljust(), 12. rjust(), 13.Strip(), 14. lstrip(), 15. rstip()
# # # 16. splite(), 17. splitlines(), 18. swapcase(), 19. startwith(), 20. endwith()
# # # 21. Count, 22. rsplit, 23. partition(), 24. Zfill(), 25. replace()
# # # 26. islower(), 27. istitle(), 28. isupper(), 29. isnumeric()
# # # 30. isdigit(), 31. isdecimal(), 32. isalpha(),33. isalnum, #isspace()

# # # 35. maketrans(), #36. translate().

# # #33. isalnum()
# # nm3="number123"
# # print(nm3.isalnum())

# # #34.
# # nm4= "          "
# # print(nm4.isspace())


# # # 1. Capitalize(), 2. Title(), 3. Upper(), 4. Lower(), 5. casefold(), 7. join(), 8. find()
# # # 9. rfind(), 10. Center(), 11. ljust(), 12. rjust(), 13.Strip(), 14. lstrip(), 15. rstip()
# # # 16. splite(), 17. splitlines(), 18. swapcase(), 19. startwith(), 20. endwith()
# # # 21. Count, 22. rsplit, 23. partition(), 24. Zfill(), 25. replace()
# # # 26. islower(), 27. istitle(), 28. isupper(), 29. isnumeric()
# # # 30. isdigit(), 31. isdecimal(), 32. isalpha(),33. isalnum, #isspace()

# # # 35. maketrans(), #36. translate().




# #                             #List


# # a=["masterShanto","Shiekh",407,856503,"Ajijul Hoque", "Shanto"]



# #                                #List, #List- Constructor

# # b=list(("masterShanto","Shiekh",407,856503,"Ajijul Hoque", "Shanto"))

# # c=list(("masterShanto","Shiekh",407,856503,"Ajijul Hoque", "Shanto"))

# # print(a,"\n",type(a))                            
# # print(c)

# ##List, #List- Constructor,#List- Nested List

# # d=["Farhana", "Akter",["masterShanto","Shiekh",407,856503], "Ajijul Hoque", "Shanto"]                            
# # print(d)

# ##List, #List- Constructor,#List- Nested List, #List- Positive Index

# # print(d[3])                            
# # print(d[3],type(d[3]))
                   
# # print(d[2][0]) # Important

            

# ##List, #List- Constructor,#List- Nested List, 
# #List- Positive Index, #List-Negetive Index

# # d=["Farhana", "Akter",["masterShanto","Shiekh",407,856503], "Ajijul Hoque", "Shanto"]
# # print(d[-3][-3])                        

# #                          #List- Range/Slice
# # print(d[2:4])
# # print(d[2][2:4])
   
#    #List, #List- Constructor,#List- Nested List, 
#    #List- Positive Index, #List-Negetive Index
#    #List- add/insert (append(),extend([]))
#    #List- Append()

# # d=["Farhana", "Akter",["masterShanto","Shiekh",407,856503], "Ajijul Hoque", "Shanto"]                        
# # d.append("Hay")
# # d.append("My Wife")
# # print(d)
#                             #List- Extend([])
# # d=["Farhana", "Akter",["masterShanto","Shiekh",407,856503], "Ajijul Hoque", "Shanto"]                        
# # d.extend([2,5,"Farhana Akter","Eity"])
# # print(d)

#                             #List-insert

# # d=["Farhana", "Akter",["masterShanto",["Discord","WhatsApp","Facebook"],"Shiekh",407,856503], "Ajijul Hoque"]

# # d[2][3]="by Insert"

# # d.insert(2,"Shanto")

# # print(d)                                 

#                             #List-Change
# # a=["Farhana", 2,["masterShanto",
# #   ["Discord",5,"Facebook"],"Shiekh",407,856503], 
# #    "Ajijul Hoque"]                            
# # print(a)
# # print()                           

# # a[2][1][1]="Five"

# # a[2:5]=["No List","No Name","CCDL Project","OHAL Project"]

# # print(a)

#                 #List-Delet (Del a[])
# # a=["Farhana", 2,["masterShanto",
# #   ["Discord",5,"Facebook"],"Shiekh",407,856503], 
# #    "Ajijul Hoque"]                            
# # del a[2][1][2]

# # print(a)                
# # print()
# # del a[2][1][2:4]
# # print(a)


#                 # list-Remove(a.remove()), for one arrgument
                
# # a=["Farhana", 2,["masterShanto",
# #   ["Discord",5,"Facebook"],"Shiekh",407,856503], 
# #    "Ajijul Hoque"]                            
# # a[2].remove("masterShanto")
# # print(a)
# #                 #List-Pop

# # a=["Farhana", 2,["masterShanto",
# #   ["Discord",5,"Facebook"],"Shiekh",407,856503], 
# #    "Ajijul Hoque"]                            
# # a.pop() #index can be use in ()
# # print(a)
# # print()

# # a.pop(2)
# # print(a)
                                
# #                 #List-Clear Method

# # a=["Farhana", 2,["masterShanto",
# #   ["Discord",5,"Facebook"],"Shiekh",407,856503], 
# #    "Ajijul Hoque"]                            
# # a.clear()
# # print(a)
          
#        #List-Loop

# # a=["Farhana", 2,["masterShanto",
# #   ["Discord",5,"Facebook"],"Shiekh",407,856503], 
# #    "Ajijul Hoque"]                            

# # # for i in a:
# # #     print(i)
# # #     print()
# # # print(a)
# # # print("*******")


# # for i in a:
# #     if type(i) is list:
# #         for j in i:
# #             if type(j) is list:
# #                 for k in j:
# #                     print(k)
# #             else:
# #                 print(j)
# #     else:
# #         print(i)


#                        #List- Length
# # a=["Farhana", 2,["masterShanto",
# #   ["Discord",5,"Facebook"],"Shiekh",407,856503], 
# #    "Ajijul Hoque"]                            

# # # Length=0

# # # for i in a:
# # #  Length+=1

# # # print(Length)                  

# # print(len(a))
# # print(len(a[2]))
# # print(len(a[2][1]))


#                        #List- Membership

# # a=["Farhana", 2,["masterShanto",
# #   ["Discord",5,"Facebook"],"Shiekh",407,856503], 
# #     "Ajijul Hoque"]

# # if "Facebook" not in a:
# #     print("Found")
# # else:
# #     print("Not Found")


#                                 # List- Repetition
# # a=["Farhana", 2,["masterShanto",
# #   ["Discord",5,"Facebook"],"Shiekh",407,856503], 
# #     "Ajijul Hoque"]                                

# # print(a[2]*2)
# # print(["Shanto"]*2)

# #                                 #List- Copy
                                
# # a=["Farhana", 2,["masterShanto",
# #   ["Discord",5,"Facebook"],"Shiekh",407,856503], 
# #     "Ajijul Hoque"]                                

# # # b=a.copy()
# # # c=a[2].copy()
# # # d=a[2][1].copy()
# # # print(b)
# # # print()
# # # print(c)
# # # print()
# # # print(d)
# # e=[]
# # for i in a:
# #     if type(i) is list:
# #         c=i.copy()
# #         print(i)
# #     else:
# #         print(i)
# # print()
# # print(c)

# #                         #List-Concatination
# # a=["Farhana", 2,["masterShanto",
# #   ["Discord",5,"Facebook"],"Shiekh",407,856503], 
# #     "Ajijul Hoque"]                        
# # b=["Add/Insert","range/Slice",
# #    "Change/Delete,membership,repetion,Length"]
# # print(b+a)


#                 #List-Methond()
# # 1. Append(), 2. extend(), 3. insert(), 4. remove(), 5. pop(), 6. clear()
# # 7. index() 

# #7. index() for single argument
# # a=["Farhana", 2,["masterShanto",
# #   ["Discord",5,"Facebook"],"Shiekh",407,856503], 
# #     "Ajijul Hoque"]                        
# # b=["Add/Insert","range/Slice",
# #     "Change/Delete","membership","repetion","Length"]
# # c=[5,20,2,23,9,3.38]
 
# # print(a.index("masterShanto"))               


# #List-Methond()
# # 1. Append(), 2. extend(), 3. insert(), 4. remove(), 5. pop(), 6. clear()
# # 7. index(), 8. Count, 9. Copy(), 10. Reverse()

# # print(a.count(2))
# # print(a.count("Farhana"))

# #9. a.copy()
# #10. reverse()
# # a.reverse()
# # print(a)


# # 11. Sort()


# # a=["Farhana", 2,["masterShanto",
# #   ["Discord",5,"Facebook"],"Shiekh",407,856503], 
# #     "Ajijul Hoque"]                        
# # b=["Add/Insert","range/Slice",
# #     "Change/Delete","membership","repetion","Length"]
# # c=[5,20,2,23,9,3.38]

# # b.sort()
# # print(b)
# # print()

# # b.sort(reverse=True)
# # print(b)
# # print()

# # b.sort(reverse=True,key=len)
# # print(b)
# # print()

# # b.sort(reverse=False,key=len)
# # print(b)
# # print()

# # c.sort()
# # print(c)
# # print()

# # c.sort(reverse=True)
# # print(c)
# # print()

# # def length(b):
# #     return len(b)
# # print()


# #List-Methond()
# # 1. Append(), 2. extend(), 3. insert(), 4. remove(), 5. pop(), 6. clear()
# # 7. index(), 8. Count, 9. Copy(), 10. Reverse(), 11. sort(), 12 sorted()

# # 12 sorted()

# # a,b,c=["Farhana", 2,["masterShanto",
# #   ["Discord",5,"Facebook"],"Shiekh",407,856503], 
# #     "Ajijul Hoque"],["Add/Insert","range/Slice",
# #     "Change/Delete","membership","repetion","Length"],[5,20,2,23,9,3.38]


# # print(sorted(c))

# # #13 Max()

# # print(max(b))


# # #14 Min()
# # print(min(b))


# # #15 Sum()

# # print(sum(c ))





# ###########List Work Finished#######################

#                                 #Tuple
# #1. Tuple-Constructore                                


# # a,b,c=("Farhana", 2,["masterShanto",
# #   ["Discord",5,"Facebook"],"Shiekh",407,856503], 
# #     "Ajijul Hoque"),("Add/Insert","range/Slice",
# #     "Change/Delete","membership","repetion","Length"),(5,20,2,23,9,3.38)
# # z=tuple(("Constructor","Magic","Range/Slice","Change"))
# # print(z)
                     
                     
# # print(a)                     
 
# # ##1. Tuple-Magic                                
                                
# # d="Shanto", 2, 5, 6,"masterShanto"                                
# # e=("Farhana",)
# # print(d,type(d))
# # print(e)
# # f=("Farhana")
# # print(f, type(f))

# ## Tuple- Nested Tuple

# # a,b,c=("Farhana", 2,["masterShanto",
# #   ("Discord",5,"Facebook"),"Shiekh",407,856503], 
# #     "Ajijul Hoque"),("Add/Insert","range/Slice",
# #     "Change/Delete","membership","repetion","Length"),(5,20,2,23,9,3.38)

# # # # Tuple- Positive Index
# # # print(a[2])



# # # #Tuple- Negetive Index

# # # print(b[-1])

# # # #Tuple- Range/Slice
# # # print(a[-2][-1])

# # # #Tuple- Add/Change/Delete
# # # #Tuple has to convert at list for add/change/delete

# # # d=list(b)

# # # d.extend(["Tuple to List","Extending"])
# # # d.append("Appended")
# # # d.remove("Length")
# # # print(d)

# # # e=tuple(d)


# # # print(e)



# # # a[2][2]="Nadira Begum"
# # # print(a)


# # # Tuple-Loop


# # # for i in a:
# # #     if type(i) is list:
# # #         for j in i:
# # #             if type(j) is tuple:
# # #                 for k in j:
# # #                     print(k)
# # #             else:
# # #                 print(j)
                
# # #     else: 
# # #         print(i)


# # # #Tuple- Membership

# # # if "Farhana" in a:
# # #     print("Found")
# # # else:
# # #     print("Note Found")

# # # #Tuple- Repetition
# # # print(c*3)

# # #Tupleo- Concatination
# # print(b+c)

# # #Tupel Method- Max() & min(), sum(), index(), sorted()

# # print(min(c))
# # print(max(c))
# # print(max(b ))
# # print(sum(c))
# # print(sum(c))
# # print(a.index("Farhana"))
# # print(sorted(c, reverse=True))



# # #Tuple-count

# # print(c.count(2))


# ######################Tuple Finished##############


#                     #Dictionary
# #1. String Key, 2. int key, 3. mix key, 4.Constructore
# #Piar                    
# # print(z)
# # print(x,type(x))

# #Dictionary -constructore
# # x={"a":"Shiekh",
# #        "b":"Ajijul",
# #        "c":"Hoque",
# #        "d":"Shanto",
# #        "z":{1:"masterShanto",
# #           "Roll NO":856503}}

# # y={1:"Farnaha",2:"Akter"}

# # z={1:"masterShanto",
# #    "Roll NO":856503}

# # a=dict({"a":"Shiekh",
# #        "b":"Ajijul",
# #        "c":"Hoque",
# #        "d":"Shanto"})
# # b=dict(v1="constructore",
# #        v2="Nested Dictionary",
# #        v3="change/add/delete")
# # c=dict([("c1","c2"),
# #         ("Rools1","Rools2"),(1,"Name")])

# # print(x)
# # print(b)

# # print(c)
#                #Dictionary
# #1. String Key, 2. int key, 3. mix key, 4.Constructore
# #Piar


# # Dictionary- Nested Dictionary

# # x={"a":["Shiekh",
# #         "Ajijul","Hoque"],
# #         "b":("Farhana","Akter","Eity"),
# #         "c":{1:"masterShanto",
# #           "Roll No.":856503}} 

# # y={1:"Farnaha",2:"Akter"}

# # z={1:"masterShanto",
# #     "Roll NO":856503}
# # print(x)
# # print()
# # print(x["a"][1])
# # print(x["a"][1][2])


# # #Dict- Accessing Value/Get()

# # print(x.get("c",[1]))


# # #Dict- Add Value

# # y[1]="Farhana Akter Eity"
 
# # print(y)


# #Dictionary-Add/Change/Del/Pop()/popiteam()

# # x={"a":["Shiekh",
# #    "Ajijul","Hoque"],
# #    "b":("Farhana","Akter","Eity"),
# #    "c":{1:"masterShanto",
# #         "Roll No.":856503}} 

# # y={1:"Farnaha",2:"Akter"}

# # z={1:"masterShanto",
# #     "Roll NO":856503}


# # x={1:"a",
# #    2:"b",
# #    3:"c",
# #    4:{"m": 535,
# #       "n": "master", 
# #       "o": "Shanto"}}

# # y={"t":[1,5,35,34]}

# # x.update(y)
# # print(x)
# # del x[1]

# # # print(x)
 
    

# # x[4].pop("n")
# # print(x)

# # #Dict - popitem()

# # x.popitem()
# # print(x)

# # print(x.keys())


# #                 #Dict- Fromkeys()
# # x={1:"a",
# #    2:"b",
# #    3:"c",
# #    4:{"m": 535,
# #       "n": "master", 
# #       "o": "Shanto"}}

# # y={"t":[1,5,35,34]}
                
# # a=("a","b","c")
# # b=dict.fromkeys(a)
# # print(b)
# # for i in b:
# #     if i=="a":
# #         b["a"]="fromkeys"
# #     elif i=="b":
# #         b["b"]="popitems()"
# #     elif i=="c":
# #         b["c"]="update()"
# # print(b)


#                      #####Set ####
# #Union
                     
# # a,b={1,3,5,8,9,11},{2,3,6,8,11}                     
# # # print(a|b)
# # # print(a.union(b))


# # #intersection

# # # print(a&b)
# # # print(a.intersection(b))

# # #Difference

# # # print(a-b)

# # #semetric Difference
# # # print(a^b)
# # print(a.symmetric_difference(b)) 


# #####Function######

# # def masterShanto():
# #     a=25
# #     b=10
# #     print("This is a Function")
# #     print(a-b)
# # def master():
# #     print(25+25)
# # master()
# # masterShanto()

# # def farhana():
# #     return "I Love You"
# # print(farhana())


# # def farhanaAkter():
# #     print("mastershanto@gmail.com")
# #     return 50*50

# # print(farhanaAkter())



# # def Bazar(ar1,ar2


# ########*arg####

# #######Functions######
# # 1. Return, 2. Arguments, 3. Parameters
# # 4. *args, 5. Keywords Arguments, 6.


# # *arg

# # def Bazar(ar1,ar2,ar3):
# #     print(ar1,ar2,ar3)
    
# # Bazar("Mango",ar2="Fish",ar3="Banana")

#      ############** Functions **##########
# # 1. Return, 2. Arguments, 3. Parameters,
# # 4. *Args, 5. Keyword Arguments 

# # def Bazar(*Arg):
    
# #     print(Arg[2])
# #     for i in Arg:
# #        print(i)       

# # Bazar("Mango","Fish","Banana")

#  ############** Functions **##########
# # 1. Return, 2. Arguments, 3. Parameters,
# # 4. *Args, 5. Keyword Arguments, 

# #5. Keyword Arguments

# # def Bazar(c1,a1,b1): #*args not work at keyword
    
# #     print(b1,c1,a1)
# # Bazar(a1="Mango",b1="Fish",c1="Banana")


# ############** Functions **##########
# # 1. Return, 2. Arguments, 3. Parameters,
# # 4. *Args, 5. Keyword Arguments / None Keyword arguments

# # def Bazar(a1,b1,c1): #*args not work at keyword
    
# #     print(c1,a1,b1)
# # Bazar("Mango",b1="Fish",c1="Banana")


# # ############** Functions **##########
# # # 1. Return, 2. Arguments, 3. Parameters,
# # # 4. *Args, 5. Keyword Arguments / None Keyword arguments
# # # 6. **kwargs

# # def Bazar(**Arg): 
    
# #     print(Arg["a1"])
# #     for i in Arg.items():
# #         print(i)
    
# # Bazar(a1="Mango",b1="Fish",c1="Banana")


# ############** Functions **##########
# # 1. Return, 2. Arguments, 3. Parameters,
# # 4. *Args, 5. Keyword Arguments / None Keyword arguments
# # 6. **kwargs

# # def Bazar(**Arg): 
    
# #     print(Arg["a1"])
# #     for i in Arg.items():
# #         print(i)
# #     print("****")
# #     for i in Arg.values():
# #         print(i)
# #     print("****")
# #     for i in Arg.keys():
# #         print(i)
    
# # Bazar(a1="Mango",b1="Fish",c1="Banana")



# ############** Functions **##########
# # 1. Return, 2. Arguments, 3. Parameters,
# # 4. *Args, 5. Keyword Arguments / None Keyword arguments
# # 6. **kwargs, 7. Defult Parameters

# # def info(Name, Subtitle = "mastershanto@gmail.com"):
# #     print(Name, Subtitle)

# # info("masterShanto","Student")
# # info("theMaster")
# # info("")

# # ############** Functions **##########
# # # 1. Return, 2. Arguments, 3. Parameters,
# # # 4. *Args, 5. Keyword Arguments / None Keyword arguments
# # # 6. **kwargs, 7. Defult Parameters, 8. pass

# # def Hey():
# #     pass
# # Hey()

# # ############** Functions **##########
# # # 1. Return, 2. Arguments, 3. Parameters,
# # # 4. *Args, 5. Keyword Arguments / None Keyword arguments
# # # 6. **kwargs, 7. Defult Parameters, 8. pass
# # # 9. Instead of return

# # # def Hellow():
# # #     return 1
# # # Hellow()
 

# # def Hellow():
# #     for i in range(0,5):
# #         yield 1
    
# # for i in Hellow():
# #     print(i)




# ############** Functions **##########
# # 1. Return, 2. Arguments, 3. Parameters,
# # 4. *Args, 5. Keyword Arguments / None Keyword arguments
# # 6. **kwargs, 7. Defult Parameters, 8. pass
# # 9. Instead of return, 10. Recurtion

# # def Hellow():
# #     return 1
# # Hellow()
 

# def Rec(N):
#     if N == 3:
#         return N
#     else:
#         return Rec(N+1)+1
    
# print(Rec(1))


# ############** Functions **##########
# # 1. Return, 2. Arguments, 3. Parameters,
# # 4. *Args, 5. Keyword Arguments / None Keyword arguments
# # 6. **kwargs, 7. Defult Parameters, 8. pass
# # 9. Instead of return, 10. Recurtion, 11. Nested Fuction

 

# def Nest(N):
#     x=10*N
    
#     def Hellow():
#         print(x*8)
#     Hellow()
#     print(x)
# Nest(5)



# ############** Functions **##########
# # 1. Return, 2. Arguments, 3. Parameters,
# # 4. *Args, 5. Keyword Arguments / None Keyword arguments
# # 6. **kwargs, 7. Defult Parameters, 8. pass
# # 9. Instead of return, 10. Recurtion, 11. Nested Fuction

# #****Nested Func,Global,Local, Nonlocal Variable****
 
# # def China():
# #    global z,m
# #    z=12
# #    m=15
# #    print("China: ",x,y,z,m)
# # def Bangladesh():
# #     global z
# #     z=13
# #     print("Bangladesh: ",x,y,z,m)

# # x=10
# # y=11
# # z=0 

# # print("Global: ",x,y,z)
# # China()
# # Bangladesh()
# # print("Global: ",x,y,z,m) 
# # China()

# def China():
#     z=12
#     def Sunghai():
#         nonlocal z
#         z=50
#         print("Sunghai: ",z)
#     Sunghai()        
#     print(z)
# China()

############** Functions **##########
# 1. Return, 2. Arguments, 3. Parameters,
# 4. *Args, 5. Keyword Arguments / None Keyword arguments
# 6. **kwargs, 7. Defult Parameters, 8. pass
# 9. Instead of return, 10. Recurtion, 11. Nested Fuction

#****Nested Func,Global,Local, Nonlocal Variable****
#Lamda (Annonimous Function)


# lambda argumens: Expression

# def Pro(a,b,c):
#     print(a+b+c)

# x=lambda a,b,c:print(a+b)
# Pro(5,6,7)
# x(5,6,7)

# print((lambda m,n,o:(m+n)*o)(2,4,5))

# def Pro(a):
#     return lambda b:b*a

# x=Pro(5)
# print(x(20))

# def Pro(a,b):
#     yield lambda a,b:b*a
    
    
# print("{:.10f}".format(2.45685))


        
          ################# MATH #################

# import math
# # print(math.ceil(5.53878994))

# print(math.floor(5.53878994))

# print(math.trunc(-3.65))
# print(math.trunc(3.65))

# a=math.modf(3.53)

# for i in a:
#     if i <1:
#         print("{:.2f}".format(i))
#     else:
#         print("Error")
    
# print(math.fabs(-50.00))    
    
# print(math.sqrt(25))
# print(math.sqrt(1313))
# print(math.isqrt(1313))
    
# print(math.pow(5,50))
# print(math.factorial(5))
# print(math.factorial(10))
# print(math.factorial(4))
# # print(math.factorial(3)
# print(math.fmod(10,3))
# print(math.fmod(11,3))
# print(math.fmod(12,3))
# print("{:.2f}".format(math.fmod(11,3)))
# print("{:*>20.2f}".format(math.fmod(11,3)))
# print("{:*^20.2f}".format(math.fsum([1+5+34+4+53+4])))
# print("{:*^20.2f}".format(math.fsum([1,5,34,4,53,4])))
# print("{:*^20.2f}".format(math.fsum([.25,5.5,34.344,4.3,53.5,4.20])))
# print("{:*^20.3f}".format(math.exp(1)))
# print("{:*^20.3f}".format(math.gcd(12,18)))
# print("{:*^20.3f}".format(math.gcd(12,18,2)))
# print("{:*^20.3f}".format(math.comb(12,2)))
# print("{:*^20.3f}".format(math.log(8)))
# print("{:*^20.3f}".format(math.log1p(7)))
# print("{:*^20.3f}".format(math.log2(8)))
# print("{:*^20.3f}".format(math.log10(10000)))
# print("{:*^20.3f}".format(math.log (10000)))
# print("{:*^20.3f}".format(math.e))
# print("{:*^20.4f}".format(math.pi))
# print("{:*^20.4f}".format(math.tau))
# print("{:*^20.4f}".format(math.tau))

# n=50

# print("{:*^20.4f}".format(math.sin(math.radians(n))))
# print("{:*^20.4f}".format(math.sin(math.radians(n))))
# print(math.tan(10))

# import time

# print(time.gmtime())
# print()




          ################### File Handaling ###################
open("master.txt","x")
File=open("master.txt","r")
print(File.read())

