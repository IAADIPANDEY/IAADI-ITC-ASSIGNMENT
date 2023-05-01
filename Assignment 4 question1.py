a= int(input("enter your marks="))
if a<0 or a>100:
   print("error")
elif a<25:
    print("Grade is E")
elif 25<=a<45:
    print ("Grade is E")
elif 45<=a<50:
    print("Grade is D")
elif 50<=a<60:
    print ("Grade is C")
elif 60<=a<80:
    print("Grade is B")
elif 80<=a:
    print("Grade is A")
