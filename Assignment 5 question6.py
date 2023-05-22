#defining a function to get a prime number
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num)):
        if num % i == 0:
            return False
    return True

#get start number
start = int(input("Enter the starting number: "))
#get ending number
end = int(input("Enter the ending number: "))

#using for loop and is_prime (defined function) to print the prime numbers
print("Prime numbers in the range", start, "to", end, "are:")
for number in range(start, end + 1):
    if is_prime(number):
        print(number)
