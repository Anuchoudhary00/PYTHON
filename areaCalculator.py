# print("*****AREA CALCULATOR*****")
# while True:
#     print(""" 1. Circle
#     2. Square   
#     3. Rectangle
#     4. Triangle""")

#     choice = int(input("Enter a number 1-4: ")) 
    
#     if choice == 1:
#       while True:
#        radius = float(input("Enter the radius of the circle: "))
#        area = 3.14 * radius * radius
#        print("The area of the circle is:", area)
      
#       repeat = input("Do you want to calculate area another circle ? (yes/no): ")
#       if repeat == "no" or repeat == "No":
#           print("Thank you for using the area calculator!")
#           break
    
#     elif choice == 2:
#       while True:  
#        side = float(input("Enter the side length of the square: "))
#        area = side**2
#        print("The area of the square is:", area)   
       
#        repeat = input("Do you want to calculate area another square ? (yes/no): ")
#        if repeat == "no" or repeat == "No":
#           print("Thank you for using the area calculator!")
#           break
    
#     elif choice == 3:
#      while True:
#       length = float(input("Enter the length of the rectangle: "))
#       width = float(input("Enter the width of the rectangle: "))
#       area = length * width
#       print("The area of the rectangle is:", area)

#       repeat = input("Do you want to calculate area another rectangle ? (yes/no): ")
#       if repeat == "no" or repeat == "No":
#           print("Thank you for using the area calculator!")
#           break
    
#     elif choice == 4:
#      while True:
#       base = float(input("Enter the base of the triangle: "))
#       height = float(input("Enter the height of the triangle: "))
#       area = 0.5 * base * height
#       print("The area of the triangle is:", area)

#       repeat = input("Do you want to calculate area another triangle ? (yes/no): ")
#       if repeat == "no" or repeat == "No":
#           print("Thank you for using the area calculator!")
#           break
# else:
#     print("Invalid choice! Please select a number between 1 and 4.")
    
#     repeat = input("Do you want to try again ? (yes/no): ")
#     if repeat == "no" or repeat == "No":
#         print("Thank you for using the area calculator!")
#         break




print("***** AREA CALCULATOR *****")

while True:
    print("""
1. Circle
2. Square
3. Rectangle
4. Triangle
""")

    choice = int(input("Enter a number 1-4: "))

    if choice == 1:
        while True:
            radius = float(input("Enter the radius of the circle: "))
            area = 3.14 * radius * radius
            print("The area of the circle is:", area)

            repeat = input("Do you want to calculate another circle? (yes/no): ")
            if repeat.lower() == "no":
                break

    elif choice == 2:
        while True:
            side = float(input("Enter the side length of the square: "))
            area = side ** 2
            print("The area of the square is:", area)

            repeat = input("Do you want to calculate another square? (yes/no): ")
            if repeat.lower() == "no":
                break

    elif choice == 3:
        while True:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = length * width
            print("The area of the rectangle is:", area)

            repeat = input("Do you want to calculate another rectangle? (yes/no): ")
            if repeat.lower() == "no":
                break

    elif choice == 4:
        while True:
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = 0.5 * base * height
            print("The area of the triangle is:", area)

            repeat = input("Do you want to calculate another triangle? (yes/no): ")
            if repeat.lower() == "no":
                break


    else:
        print("Invalid choice! Please select between 1 and 5.")
        
    repeat = input("Do you want to try again? (yes/no): ")
    if repeat.lower() == "no":          
        print("Thank you for using the area calculator!")
        break