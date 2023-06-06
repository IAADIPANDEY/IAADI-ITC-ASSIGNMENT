# Defining function
def is_perfect_number(number):
    if number <=0:
        return False
    # calculate the sum of proper positive divisors
    divisors_sum = sum(i for i in range(1,number) if number%i==0)
    # check if the sum of proper positive divisors is equal to the no. itself
    if divisors_sum == number:
        print("It is Perfect No")
    else:
        print("It is not a  Perfect No")

# calling the function
a = int(input())
is_perfect_number(a)
