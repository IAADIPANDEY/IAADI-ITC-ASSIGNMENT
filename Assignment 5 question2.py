#get n1 for starting range
n1 = int(input("Enter starting number : "))
#get n2 for ending range
n2 = int(input("Enter ending number : "))
#get the divisor number
n = int(input("Enter divisor number : "))
#using for loop and modulus operator for geting output
for i in range(n1, n2+1):
    if i%n==0:
        print(i)
