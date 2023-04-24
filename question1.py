# Ques 1
str = "Python is a case sensitive language"
print(len(str))         # Length of the input string


reversed_string = str[::-1]
# Slice the array from the 1st element to the last element in reverse order.
print(reversed_string)


# print(str.index('a'))
new_str = str[10:len(str)]
print(new_str)


oop_Str = str[0:12] + "object oriented"
print(oop_Str)


print(str.index('a'))

no_space_str = str.replace(" ","")
print(no_space_str)