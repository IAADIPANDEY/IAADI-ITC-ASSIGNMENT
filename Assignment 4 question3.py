import random
import math

count=0
while count<10:
    count =count+1
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    guess= int(input("what is " + str(num1) + "x"+ str(num2) +"="))
    ans = int(num1*num2)
    correct = guess == ans
    if (guess== ans):
        print ("correct")
    else:
        print("wrong, the answer is " + str(ans) + ",")