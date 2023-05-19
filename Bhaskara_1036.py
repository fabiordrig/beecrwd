import math

a, b, c = map(float, input().split())

# Calculation of delta
delta = b**2 - 4 * a * c

# Check if it is possible to calculate the roots
if a == 0 or delta < 0:
    print("Unable to calculate")
else:
    # Calculation of the roots
    root1 = (-b + math.sqrt(delta)) / (2 * a)
    root2 = (-b - math.sqrt(delta)) / (2 * a)

    # Printing the results with 5 decimal places
    print("R1 = {:.5f}".format(root1))
    print("R2 = {:.5f}".format(root2))
