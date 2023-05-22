rows = 5
#defining for loop for printing stars in pattern given as output
for i in range(1, rows * 2):
    if i <= rows:
        print("* " * i)
    else:
        print("* " * (2 * rows - i))