name = input("enter your name:")
print(f"\nwelcome,{name}!")

print("""
choose a shape:

      
1. Left Triangle

2. right triangle
3. inverted left triangle
4. inverted right triangle)
5. pascal's left triangle
6. pascal's right trianle
7. diamond
8. pyramid
9. double pyramid
10. inverted pyramid
11. inverted double pyramid
12. hour glass
""")
choice = int(input("enter the number corresponding to your choice: "))
rows = int(input("enter the number of rows: "))

# Left Triangle
if choice == 1:
    i = 1
    while i <= rows:
        print("*" * i)
        i += 1

# Right Triangle
elif choice == 2:
    i = 1
    while i <= rows:
        print(" " * (rows - i) + "*" * i)
        i += 1

# Inverted Left Triangle
elif choice == 3:
    i = rows
    while i >= 1:
        print("*" * i)
        i -= 1

# Inverted Right Triangle
elif choice == 4:
    i = rows
    while i >= 1:
        print(" " * (rows - i) + "*" * i)
        i -= 1

# Pascal's Left Triangle
elif choice == 5:
    i = 1
    while i <= rows:
        print("*" * i)
        i += 1

    i = rows - 1
    while i >= 1:
        print("*" * i)
        i -= 1

# Pascal's Right Triangle
elif choice == 6:
    i = 1
    while i <= rows:
        print(" " * (rows - i) + "*" * i)
        i += 1

    i = rows - 1
    while i >= 1:
        print(" " * (rows - i) + "*" * i)
        i -= 1

# Diamond
elif choice == 7:
    i = 1
    while i <= rows:
        print(" " * (rows - i) + "*" * (2 * i - 1))
        i += 1

    i = rows - 1
    while i >= 1:
        print(" " * (rows - i) + "*" * (2 * i - 1))
        i -= 1

# Pyramid
elif choice == 8:
    i = 1
    while i <= rows:
        print(" " * (rows - i) + "*" * (2 * i - 1))
        i += 1

# Double Pyramid
elif choice == 9:
    i = 1
    while i <= rows:
        left = "*" * (2 * i - 1)
        middle = " " * (2 * (rows - i) + 1)
        right = "*" * (2 * i - 1)
        print(left + middle + right)
        i += 1

# Inverted Pyramid
elif choice == 10:
    i = rows
    while i >= 1:
        print(" " * (rows - i) + "*" * (2 * i - 1))
        i -= 1

# Inverted Double Pyramid
elif choice == 11:
    i = rows
    while i >= 1:
        left = "*" * (2 * i - 1)
        middle = " " * (2 * (rows - i) + 1)
        right = "*" * (2 * i - 1)
        print(left + middle + right)
        i -= 1

# Hour Glass
elif choice == 12:
    i = rows
    while i >= 1:
        print(" " * (rows - i) + "*" * (2 * i - 1))
        i -= 1

    i = 2
    while i <= rows:
        print(" " * (rows - i) + "*" * (2 * i - 1))
        i += 1

else:
    print("Invalid Choice")