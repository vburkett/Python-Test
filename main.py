import minemath
a = float(input("Enter a number A for (Ax+B=0): "))
b = float(input("Enter a number B for (Ax+B=0): "))

x = minemath.SolveAxplusB(a,b)
print("The solution for x is...")
print(x)

print()

a = float(input("Enter a value for A in the form (A^2+B^2=C^2): "))
b = float(input("Enter a value for B in the form (A^2+B^2=C^2): "))

c = minemath.SolveHypotenuse(a,b)
print("The solution for c is...")
print(c)