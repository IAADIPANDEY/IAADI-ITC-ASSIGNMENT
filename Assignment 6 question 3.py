# Defing function
def print_pascals_triangle(n):
    # Create an empty list to store each row of the triangle
    triangle = []
    for i in range(n):
        # Creating a new row and initializing it with 1
        row = [1]
        # Generate the value for the row based on previous raw
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(len(prev_row) - 1):
                # Calculating the value by adding the two number above it
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
        triangle.append(row)

    max_width = len(str(triangle[-1][len(triangle[-1]) // 2])) + 1

    for i in range(n):
        row = triangle[i]
        padding = ' ' * ((n - i - 1) * max_width // 2)
        line = ' ' * (max_width // 2)
        for num in row:
            line += str(num).center(max_width)
        print(padding + line)

print_pascals_triangle(9)
