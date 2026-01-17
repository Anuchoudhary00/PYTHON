print("*****AREA CALCULATOR*****")
print(""" 1. Circle
2. Square   
3. Rectangle
4. Triangle""")

choice = int(input("Enter a number 1-4: ")) 
if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius * radius
    print("The area of the circle is:", area)
    
elif choice == 2:
    side = float(input("Enter the side length of the square: "))
    area = side**2
    print("The area of the square is:", area)   
    
elif choice == 3:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print("The area of the rectangle is:", area)
    
elif choice == 4:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is:", area)
    
else:
    print("Invalid choice! Please select a number between 1 and 4.")
