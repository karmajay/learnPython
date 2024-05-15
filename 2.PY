#STRINGS

#STRING IS DATA TYPE THAT STORES A SQUENCE OF CHARACTERS.\

#THEIR ARE THREE TYPES OF STRINGS

#1st 

# str1 = "first"  #jyadatar yeh vali strig hi use ki jati hai
# str2 = 'second'
# str3 = """thired"""

#apni string ke andar next line lane ke liye \n isse next line ajayegi
#EXAMPLE

# print("my name is jay karma \nand my age is 17")  

#CONCATENATION - means do strings ko apas me jodna

# str1 = "jay"
# str2 = "karma"
# print(str1+str2) #LIKE THIS HAHA

#LENGTH OF STR  #MEANS YE KISI BHI STRIN KI LENGTH KO CALCULATE KARNE KE KAAM ATA HAI

#LIKE THIS 

# str1 = "hello"
# len1 = len(str1)

# print(len1)

#INDEXING - means ki hamare konse number par konsa character hai and numbers start with "0"

# str = "jaykarma"
# print(str[0]) 

#SLICING   - means jab bhi hum string ke tukde karte he use hum slicing kehate hai

# str = "jayukarma"
# print(str[4:9])    #agar hum ending index nahi likhege to automatic last tak count ho jayega or agar starting kuch nahi likhenge to vo samjhega ki 0 se start karna hai
# #like this
# print(str[4:])     #iska matlb pura karma count ho jayega
# print(str[:4])     #iska matlb pura jayu count ho jayega 


#SLICING NEGATIVE CASE   # BAAD ME SIKHENGE

#STRING FUNCTION

#1st FUNCTION

# str = "my name is jay karma"
# print(str.endswith("a"))   #this function help us to find ki string me last word ya letter jo value likhi hai usse end hota hai ya nahi

#2nd FUNCTION

# str = "my name is jay karma"
# print(str.capitalize())    #with the help of this function we can capitalize our first str letter.

#3rd FUNCTION
# str = "my name is jay karma"
# print(str.replace("jay karma","sagar karole"))  #with the help of this function we can replace any word.

# #4th FUNCTION

# str = "my name is jay karma"
# print(str.find("is"))  #with the help of this function we can find any word.

#5th FUNCTION

# str = "my name is jay karma and my collage name is MNDC"
# print(str.count("name"))   #with the help of this function hum pata laga sakte hai ki koi word kitni baar use hua he.

#PRACTICE QUESTION'S

#1st QUESTION

# WRITE A PROGRAM TO INPUT USER'S FIRST NAME & PRINT ITS LENGTH.

#SOLUTION

# first = input("name")
# print(len(first))        

#2nd QUESTION

#WRITE A PROGRAM TO FIND THE OCCURENCE OF '$' IN A STRING

# first = "i want 50$ $ $"
# print(first.count("$"))

#CONDITIONAL STATEMENTS 

# {IF} {ELIF} {ELSE}   'SYNTAX'

#1st {IF}

# age = 21

# if(age >= 18):
#     print("can vote and apply for license")  # means agar ye kaam sach he to yaha parr true hona chahiye

#2nd  {elif}   #elif ko likhne se pehale i likhna jaruri hai

# light = "green"
# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("look or wait")
# elif(light == "green"):
#     print("GO")        

#3rd {ELSE}   else lo sirf ek baar likhte hai or last me lihkte hai

# light = "pink"
# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("look or wait")
# elif(light == "green"):
#     print("GO")
# else:
#     print("light was broken")     

#EXAMPLE

# age = 17
# if(age >= 18):
#     print("can vote")
# else:
#     print("cannot vote")    

# CONDITIONAL STATEMENTS EXAMPLE

#GRADE STUDENTS BASED ON THEIR MARKS 

# marks = int(input("student marks :"))
# if (marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"
# print("grade of the student is -->",grade)                

#NESTING - means ek statement ke andar dusri statement ko likhna

#example

# age = 100

# if(age >= 18):
#     if(age >= 80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")

#PRACTICE QUESTION

#!st QUESTION

# WRITE A PROGRAM TO CHECK IF A NUMBER ENTERD BY THE USER IS ODD OR EVEN.

#ANSWERE

# num = int(input("enter number :"))

# if(num % 2 == 0):
#     print("EVEN")
# else:
#     print("ODD")    

#NEXT QUESTION

# 2nd QUESTION

#WRITE A PROGRAM TO FIND THE GREATEST OF 3 NUMBERS ENTERED BY THE USERS 

# a = int(input("enter first num :"))
# b = int(input("enter second num :"))
# c = int(input("enter third num :"))
# d = int(input("enter fourth num :"))

# if(a >= b and a >= c and a >= d):
#     print("'a' is the greatest num")
# elif(b >= c and b >= d):
#     print("'b' is the greatest num")
# elif(c >= d):
#     print("'c' is the largest num")
# else:
#     print("d is the largest no")

#3rd QUESTION 

#WRITE A PROGRAM TO CHECK IF NUMBER IS A MULIPLE OF 7 OR NOT.

# num = int(input("enter your numbere"))

# if(num % 5 == 0):
#     print("multiple")
# else:
#     print("not a multiple")    

print(2 + 3)

























