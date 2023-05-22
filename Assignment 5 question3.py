#defining a function for area of a triangle
def calculate_triangle_area(a, b, c):
    # Check if the combination of sides is possible
    if a + b > c and b + c > a and c + a > b:
        s = (a + b + c) / 2     # Calculate the semi-perimeter

        # Calculate the area using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c))**0.5
        return area
    else:
        return "Invalid combination of sides"

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

area = calculate_triangle_area(a, b, c)
print("Area of the triangle:", area)
