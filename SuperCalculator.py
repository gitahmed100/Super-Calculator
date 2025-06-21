import functions
from functions import *

nm = input("what is your name? ")
print("welcome,", nm)
while True:
    print("press 0 to shutdown the program")
    print("press 1 to reach the password generator service")
    print("press 2 to reach the calculator")
    print("press 3 to reach the clock service")
    print("press 4 to reach the alarm service")
    print("press 5 to reach the timer service")
    print("press 6 to reach the count words service")
    print("")

    U = int(input("choose the service you need from 1 to 6: "))
    print("")

    # password generator:

    if U == 1:
        print("sure")
        import random

        main()
        print("")








    # calculator

    elif U == 2:
        print("sure")
        print("")
        print("press 0 to calculate digits")
        print("press 1 to calculate area of shapes")
        print("press 2 to calculate circumference of a circle")
        print("press 3 to calculate perimeter of shapes")
        print("press 4 to calculate volume of shapes")
        print("press 5 to convert measuring units")
        print("press 6 to convert time units")
        print("press 7 to calculate GPA")
        print("press 8 to calculate current intensity")
        print("press 9 to calculate distance")
        print("")

        chs = int(input("what do you want me to do? "))
        print("")

        # calculate digits:           #ahmed niazy

        if chs == 0:
            print("type 1 for addition of 2 numbers operation")
            print("type 2 for the subtraction of 2 numbers operation")
            print("type 3 for the multiplication of 2 numbers operation")
            print("type 4 for the division of 2 numbers operation")

            s = int(input("select the operation wanted by typing the number that refers to it (from 1 to 4 only): "))
            print(correct_input_1(s))
            print("")

            if s == 1:  # addition
                print("addition operation is in progress")
                num1 = float(input("enter the first number: "))
                num2 = float(input("enter the second number: "))
                print(sum(num1, num2))
                print("")

            elif s == 2:  # subtraction
                print("subtraction operation is in progress")
                num1 = float(input("enter the first number: "))
                num2 = float(input("enter the second number: "))
                print(subtraction(num1, num2))
                print("")


            elif s == 3:  # multiplication
                print("multiplication operation is in progress")
                num1 = float(input("enter the first number: "))
                num2 = float(input("enter the second number: "))
                print(multiplication(num1, num2))
                print("")


            elif s == 4:  # division
                print("division operation is in progress")
                num1 = float(input("enter the first number: "))
                num2 = float(input("enter the second number: "))
                print(division(num1, num2))
                print("")


            else:
                exit


        # calculate area                  #ahmed niazy

        elif chs == 1:
            print("sure😊")
            print("")

            print("type 1 to find the area of the square")
            print("type 2 to find the area of rectangle")
            print("type 3 to find the area of circle")
            print("type 4 to find the area of triangle")
            print("type 5 to find the area of parallelogram")
            print("type 6 to find the area of trapezium")
            print("type 7 to find the area of rhombus")
            print("type 8 to find the area of sphere")
            print("type 9 to find the total surface area of cube")
            print("type 10 to find the area of kite")
            print("")

            w = int(input("select the number of the shape you want to find the area for(from 0 to 10 only): "))
            print("")

            if w == 1:  # area of square

                print("calculating square area is in progress")
                s1 = float(input("enter the side length: "))
                print(area_square(s1))
                print("")






            elif w == 2:  # rectangle

                print("calculating rectangle area is in progress")
                l = float(input("enter the length: "))
                w = float(input("enter the width: "))
                print(area_rectangle(l, w))
                print("")





            elif w == 3:  # circle

                print("calculating area of circle in progress")
                r = float(input("enter the radius of the circle: "))
                print(area_circle(r))
                print("")






            elif w == 4:  # triangle

                print("calculating area of triangle in progress")
                b = float(input("enter the base length of the triangle: "))
                h = float(input("enter the height length of the triangle: "))
                print(area_triangle(b, h))
                print("")








            elif w == 5:  # parallelogram

                print("calculating area of parallelogram in progress")
                b = float(input("enter the base length of the parallelogram: "))
                h = float(input("enter the height length of the parallelogram: "))
                print(area_parallelogram(b, h))
                print("")








            elif w == 6:  # trapezium

                print("calculating area of trapezium in progress")
                s1 = float(input("enter the first side length of the trapezium: "))
                s2 = float(input("enter the second side length of the trapezium: "))
                h = float(input("enter the height length of the trapezium: "))
                print(area_trapezium(s1, s2, h))
                print("")







            elif w == 7:  # rhombus

                print("calculating area of rhombus in progress")
                diagonal_1 = float(input("enter the length of the first diagonal: "))
                diagonal_2 = float(input("enter the length of the second diagonal: "))
                print(area_rhombus(diagonal_1, diagonal_2))
                print("")







            elif w == 8:  # sphere

                print("calculating area of sphere in progress")
                r = float(input("enter the radius length of the sphere: "))
                print(area_sphere(r))
                print("")








            elif w == 9:  # cube

                print("calculating total surface area of the cube in progress")
                s = float(input("enter the side length of the cube: "))
                print(total_surface_area_for_cube(s))
                print("")







            elif w == 10:  # kite

                print("calculating area of kite in progress")
                diagonal_1 = float(input("enter the length of the first diagonal: "))
                diagonal_2 = float(input("enter the length of the second diagonal: "))
                print(area_kite(diagonal_1, diagonal_2))
                print("")










        # option to calculate circumference of a circle:          #ahmed niazy

        elif chs == 2:

            print("sure😊")
            print("")

            print("calculating the circumference of the circle is in progress")
            r = float(input("enter the radius of the circle to find circumference for: "))
            print(circum_circle(r))
            print("")










        # option to calculate perimeter of shapes:         #ahmed niazy

        elif chs == 3:
            print("sure😊")
            print("")

            print("type 1 to find the perimeter of the square")
            print("type 2 to find the perimeter of rectangle")
            print("type 3 to find the perimeter of triangle")
            print("type 4 to find the perimeter of parallelogram")
            print("type 5 to find the perimeter of trapezium")
            print("type 6 to find the perimeter of rhombus")
            print("")

            w = int(input("select the number of the shape you want to find the perimeter for(from 1 to 6 only): "))
            print("")

            if w == 1:

                print("calculating square perimeter is in progress")
                s = float(input("enter the side length: "))
                print(per_square(s))
                print("")







            elif w == 2:

                print("calculating rectangle perimeter is in progress")
                l = float(input("enter the length: "))
                w = float(input("enter the width: "))
                print(per_rectangle(l, w))
                print("")


            elif w == 3:

                print("calculating perimeter of triangle in progress")
                b = float(input("enter the base length of the triangle: "))
                s1 = float(input("enter the first side length of the triangle: "))
                s2 = float(input("enter the second side length of the triangle: "))
                print(per_triangle(b, s1, s2))
                print("")



            elif w == 4:

                print("calculating perimeter of parallelogram in progress")
                b = float(input("enter the base length of the parallelogram: "))
                s = float(input("enter the side length of the parallelogram: "))
                print(per_parallelogram(b, s))
                print("")



            elif w == 5:

                print("calculating perimeter of trapezium in progress")
                s1 = float(input("enter the first side length of the trapezium: "))
                s2 = float(input("enter the second side length of the trapezium: "))
                b1 = float(input("enter the first base length of the trapezium: "))
                b2 = float(input("enter the second base length of the trapezium: "))
                print(per_trapezium(s1, s2, b1, b2))
                print("")




            elif w == 6:

                print("calculating perimeter of rhombus in progress")
                s = float(input("enter the side length of the rhombus: "))
                print(per_rhombus(s))
                print("")





            else:
                print("error not valid,enter a valid number")
                print("")


        # to calculate volume:                     #ahmed ihab

        elif chs == 4:
            print("Sure😊")
            print("cube, sphere, cylinder, cone, pyramid")
            sh = input("what is the shape you want to calculate its volume ?")
            print("")
            import math

            # Cube:

            if sh == "cube":

                side_length = float(input("Enter the side length of the cube: "))
                volume = cube_volume(side_length)
                print(f"Volume of the cube: {volume}")
                print("")



            # Sphere :

            elif sh == "sphere":

                radius = float(input("Enter the radius of the sphere: "))
                volume = sphere_volume(radius)
                print(f"Volume of the sphere: {volume}")
                print("")



            # Cylinder :

            elif sh == "cylinder":

                radius = float(input("Enter the radius of the cylinder: "))
                height = float(input("Enter the height of the cylinder: "))
                volume = cylinder_volume(radius, height)
                print(f"Volume of the cylinder: {volume}")
                print("")


            # Cone :

            elif sh == "cone":

                radius = float(input("Enter the radius of the cone: "))
                height = float(input("Enter the height of the cone: "))
                volume = cone_volume(radius, height)
                print(f"Volume of the cone: {volume}")
                print("")


            # Pyramid :

            elif sh == "pyramid":

                base_length = float(input("Enter the base length of the pyramid: "))
                base_width = float(input("Enter the base width of the pyramid: "))
                height = float(input("Enter the height of the pyramid: "))
                volume = pyramid_volume(base_length, base_width, height)
                print(f"Volume of the pyramid: {volume}")
                print("")

            else:
                print("sorry can't help you with that 😞")
                print("")





        elif chs == 5:  # to convert measuring units:          #adel akram
            print("Sure😊")
            print("")

            cmu()
            print("")






        elif chs == 6:  # Time converter :            #ahmed ihab
            print("sure😊")
            print("")

            time_converter()
            print("")









        elif chs == 7:  # gpa calculator      #ahmed ihab
            print("Sure😊")
            print("")

            calculate_gpa()
            print("")











        elif chs == 8:  # option to calculate current intensity:              #ahmed niazy

            print("finding the current intensity is in progress")
            v = float(input("enter the lamp voltage: "))
            r = float(input("enter the lamp resistance: "))
            print(current_intensity_finder(v, r))
            print("")



        elif chs == 9:  # calculate distance      #adel akram
            print("Sure😊")
            print("")

            dist()
            print("")

        else:
            print("Sorry, but can't do that in the mean time😞")
            print("")




    elif U == 3:  # adel akram       #clock
        print("sure")
        from tkinter import *
        from tkinter.ttk import *
        from time import strftime

        root = Tk()  # creat window
        root.title("clock")  # name the window


        def time():  # clock function
            string = strftime('%H:%M:%S %p')  # time text formate
            Label.config(text=string)  # display time
            Label.after(1000, time)  # function delay           #1000 = 1sec


        Label = Label(root, font=("ds-digital", 80), background="black", foreground="blue")  # text discription
        Label.pack(anchor='center')  # location
        time()

        mainloop()




    elif U == 4:  # adel akram          # alarm
        print("sure")
        print("")
        alarm()
        print("")




    elif U == 5:  # adel akram       # timer
        print("sure")
        print("")

        t = input("enter time in seconds: ")

        countdown(int(t))
        print("")











    elif U == 6:  # ahmed ihab        #word counter
        print("sure")
        print("")
        print("press 1 if you want to write your sentence in the program")
        print("press 2 if you want to count words from external text file")
        print("")
        chs = int(input("press here: "))


        def word_count():  # function to count words
            if chs == 1:
                sent = input("type your words: ").split()
                cont = 0
                for i in sent:
                    cont += 1
                print("number of words= ", cont)
            elif chs == 2:
                file = open(input("enter the path of your file: "))
                count = 0
                for line in file:
                    words = line.split()
                    count += len(words)
                print("number of words= ", count)
            while chs != 1 and chs != 2:
                print("invalid input try again")
                break


        word_count()
        print("")



    elif U == 0:
        print("closing programm")
        break

    else:
        print("invalid input!......please type numbers from 1 to 6")
        print("")