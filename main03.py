
import cmath

user = input('Enter your name : ')
print(f'Dear {user}! In this porgram you can solve a custom quadratic polynomial writtend in the format of ')
print("Format: ax² + bx + c = 0\n")

a = float(input('Enter coefficient (a) : '))
b = float(input('Enter coefficient (b) : '))
c = float(input('Enter coefficient (c) : '))

print(f'Dear {user} the following equation is {a}x² + {b}x + {c} : ')

solutuion = (b**2) - (4 * a * c)

if a == 0:
    print(f'Dear {user} the following equation ({a}x² + {b}x + {c}), has 0 in {a}!! Which is not a quadratic polynoail it is linear :')

elif solutuion > 0:
    root1 = (-b + cmath.sqrt((solutuion)) / (2 * a) )
    root2 = (-b + cmath.sqrt((solutuion)) / (2 * a) )
    print(f"Result: The equation has TWO real roots.")
    print(f"x = {root1}")
    print(f"x = {root2}")

elif solutuion == 0:
    root = -b / (2 * a)
    print(f"Result: The equation has ONE real root.")
    print(f"x = {root}")

else:
    print("Result: The equation has NO real roots (the roots are complex numbers).")