numbers = []#taking an empty list
#using for loop and append operator to get elements in list
for i in range(10):
    num = int(input("Enter an integer: "))
    numbers.append(num)

positive_numbers = [num for num in numbers if num > 0]#using if condition to get positive numbers in the list
negative_numbers = [num for num in numbers if num < 0]#using if condition to get negative numbers in the list
odd_numbers = [num for num in numbers if num % 2 != 0]#using if condition to get odd numbers in the list
even_numbers = [num for num in numbers if num % 2 == 0]#using if condition to get even numbers in the list

#using for loop and get operator to get the number of repeated numbers
occurrences = {}
for num in numbers:
    occurrences[num] = occurrences.get(num, 0) + 1

print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)
print("Number of occurrences:")
for num, count in occurrences.items():
    print(num, "occurs", count, "times")