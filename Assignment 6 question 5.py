str1 = input()
list = str1.split("-") # split the string into individual words 
lis = sorted(list) # sort the word alphabatically
str2 = "-".join(lis) # join the sorted words with ahyphen seperated sequence
print(str2)
