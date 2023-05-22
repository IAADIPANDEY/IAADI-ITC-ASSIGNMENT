#ddefining a function to print the required pattern as output
def print_alphabet_triangle(rows):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0
    for i in range(1, rows + 1):
        for j in range(i):
            print(alphabet[count % 26], end='')
            count += 1
        print()

rows = int(input("Enter the number of rows: "))
print_alphabet_triangle(rows)