#defining a function to get reverse string
def reverse_string(string):
    return string[::-1]


#get input string
str = input("Enter a string to reverse : ")
rev_str = reverse_string(str)
print(f"Reversed string is : {rev_str}")