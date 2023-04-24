# Ques 6
side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))

# Check if the given input lengths can form a triangle
if (side1 > side2 + side3) or (side2 > side1 + side3) or (side3 > side1 + side2):
    print("No")
else:
    print("Yes")