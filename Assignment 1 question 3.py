# calculating the number of minutes and seconds

seconds = int(input("Enter the number of seconds: "))

minutes = seconds // 60    # // is integer division
remaining_seconds = seconds % 60  # using modulus operator to get remainder
# here seconds , minutes, remaining_seconds are varaibles defined 

print(f"{seconds} seconds is {minutes} minutes and {remaining_seconds} seconds")
# using f string to print the result
