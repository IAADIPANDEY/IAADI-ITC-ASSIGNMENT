#  using math function
import math
for angle in range(0, 346, 15):
#  using for loop
    radians=math.radians(angle)
    sine=round(math.sin(radians),4)
    cosine=round(math.cos(radians),4)
    print(f"{angle}, {sine}, {cosine}")
    #  using f string to get output



