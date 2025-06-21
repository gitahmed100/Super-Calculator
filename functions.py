import random
import math

def generate_passwords(number, length):  # ahmed ihab
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%/?>:(){}[]0123456789"
    passwords_list = []

    for i in range(number):
        password = ""
        for i in range(length):
            password += random.choice(chars)
        passwords_list.append(password)

    return passwords_list


def main():
    number = int(input("Amount of passwords to generate: "))
    length = int(input("Enter your password length: "))

    while number == 0 or length == 0:
        print("Invalid input")
        number = int(input("Amount of passwords to generate: "))
        length = int(input("Enter your password length: "))

    generated_passwords = generate_passwords(number, length)

    for password in generated_passwords:
        print("\nHere are your passwords:", password)


def sum(num1, num2):  # function to perform summation
    sum = num1 + num2
    return sum


def subtraction(num1, num2):  # function to perform subtraction
    subtraction = num1 - num2
    return subtraction


def multiplication(num1, num2):  # function to perform multiplication
    multiplication = num1 * num2
    return multiplication


def division(num1, num2):  # function to perform division
    division = num1 / num2
    return division


def correct_input_1(s):  # function ask the user to correct his input if he entered an invalid input
    while s < 0 or s > 8:
        s = int(input(
            'error!,please enter a valid number from 0 to 8 and type it to the program once more to be confirmed :'))
    return s


def area_square(s1):  # function to calculate area of square
    area_square = s1 ** 2
    return area_square


def area_rectangle(l, w):  # function to calculate area of rectangle
    area_rectangle = l * w
    return area_rectangle


def area_circle(r):  # function to calculate area of circle
    area_circle = 3.14 * r * r
    return area_circle


def area_triangle(b, h):  # function to calculate area of triangle
    area_triangle = 0.5 * b * h
    return area_triangle


def area_parallelogram(b, h):  # function to calculate area of parallelogram
    area_parallelogram = b * h
    return area_parallelogram


def area_trapezium(s1, s2, h):  # function to calculate area of trapezium
    area_trapezium = 0.5 * (s1 + s2) * h
    return area_trapezium


def area_rhombus(diagonal1, diagonal2):  # function to calculate area of rhombus
    area_rhombus = (diagonal1 * diagonal2) / 2
    return area_rhombus


def area_sphere(r):  # function to calculate sphere
    area_sphere = 4 * 3.14 * r * r
    return area_sphere


def total_surface_area_for_cube(s):  # function to calculate total surface area of cube
    total_surface_area_for_cube = 6 * s * s
    return total_surface_area_for_cube


def area_kite(diagonal1, diagonal2):  # function to calculate area of kite
    area_kite = (diagonal1 * diagonal2) / 2
    return area_kite


def circum_circle(r):  # function to calculate circumference
    circum_circle = 2 * 3.14 * r
    return circum_circle


def per_square(s):
    per_square = 4 * s
    return per_square


def per_rectangle(l, w):
    per_rectangle = 2 * (l + w)
    return per_rectangle


def per_triangle(b, s1, s2):
    per_triangle = b + s1 + s2
    return per_triangle


def per_parallelogram(b, s):
    per_parallelogram = 2 * (b + s)
    return per_parallelogram


def per_trapezium(s1, s2, b1, b2):
    per_trapezium = s1 + s2 + b1 + b2
    return per_trapezium


def per_rhombus(s):
    per_rhombus = 4 * s
    return per_rhombus


def cube_volume(side_length):
    return side_length ** 3


def sphere_volume(radius):
    return (4 / 3) * math.pi * radius ** 3


def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height


def cone_volume(radius, height):
    return (1 / 3) * math.pi * radius ** 2 * height


def pyramid_volume(base_length, base_width, height):
    return (1 / 3) * base_length * base_width * height


def cmu():  # adel akram
    print("tera, giga, mega, kilo, oringinal, centi, milli, micro, nano, picro")
    fr = input("what is the unit you have? ")
    to = input("what is the unit to convert it to? ")
    f = int(input("enter the number: "))

    # from tera to the rest:

    if fr == "tera" and to == "giga":
        t = f * (10 ** 3)
        print("The number = ", t)
    elif fr == "tera" and to == "mega":
        t = f * 10 ** 6
        print("The number = ", t)
    elif fr == "tera" and to == "kilo":
        t = f * 10 ** 9
        print("The number = ", t)
    elif fr == "tera" and to == "original":
        t = f * 10 ** 12
        print("The number = ", t)
    elif fr == "tera" and to == "centi":
        t = f * 10 ** 14
        print("The number = ", t)
    elif fr == "tera" and to == "milli":
        t = f * 10 ** 15
        print("The number = ", t)
    elif fr == "tera" and to == "micro":
        t = f * 10 ** 18
        print("The number = ", t)
    elif fr == "tera" and to == "nano":
        t = f * 10 ** 21
        print("the number = ", t)
    elif fr == "tera" and to == "picro":
        t = f * 10 * 24
        print("The number = ", t)

    # from giga to the rest:

    elif fr == "giga" and to == "tera":
        t = f * 10 ** -3
        print("The number = ", t)
    elif fr == "giga" and to == "mega":
        t = f * 10 ** 3
        print("The number = ", t)
    elif fr == "giga" and to == "kilo":
        t = f * 10 ** 6
        print("The number = ", t)
    elif fr == "giga" and to == "original":
        t = f * 10 ** 9
        print("The number = ", t)
    elif fr == "giga" and to == "centi":
        t = f * 10 ** 11
        print("The number = ", t)
    elif fr == "giga" and to == "milli":
        t = f * 10 ** 12
        print("The number = ", t)
    elif fr == "giga" and to == "micro":
        t = f * 10 ** 15
        print("The number = ", t)
    elif fr == "giga" and to == "nano":
        t = f * 10 ** 18
        print("The number = ", t)
    elif fr == "giga" and to == "picro":
        t = f * 10 ** 21
        print("The number = ", t)

    # from mega to the rest:

    elif fr == "mega" and to == "tera":
        t = f * 10 ** -6
        print("The number = ", t)
    elif fr == "mega" and to == "giga":
        t = f * 10 ** -3
        print("The number = ", t)
    elif fr == "mega" and to == "kilo":
        t = f * 10 ** 3
        print("The number = ", t)
    elif fr == "mega" and to == "original":
        t = f * 10 ** 6
        print("The number = ", t)
    elif fr == "mega" and to == "centi":
        t = f * 10 ** 8
        print("The number = ", t)
    elif fr == "mega" and to == "milli":
        t = f * 10 ** 9
        print("The number = ", t)
    elif fr == "mega" and to == "micro":
        t = f * 10 ** 12
        print("The number = ", t)
    elif fr == "mega" and to == "nano":
        t = f * 10 ** 15
        print("The number = ", t)
    elif fr == "mega" and to == "picro":
        t = f * 10 ** 18
        print("The number = ", t)

    # from kilo to the rest:

    elif fr == "kilo" and to == "tera":
        t = f * 10 ** -9
        print("The number = ", t)
    elif fr == "kilo" and to == "giga":
        t = f * 10 ** -6
        print("The number = ", t)
    elif fr == "kilo" and to == "mega":
        t = f * 10 ** -3
        print("The number = ", t)
    elif fr == "kilo" and to == "original":
        t = f * 10 ** 3
        print("The number = ", t)
    elif fr == "kilo" and to == "centi":
        t = f * 10 ** 5
        print("The number = ", t)
    elif fr == "kilo" and to == "milli":
        t = f * 10 ** 6
        print("The number = ", t)
    elif fr == "kilo" and to == "micro":
        t = f * 10 ** 9
        print("The number = ", t)
    elif fr == "kilo" and to == "nano":
        t = f * 10 ** 12
        print("The number = ", t)
    elif fr == "kilo" and to == "picro":
        t = f * 10 ** 15
        print("The number = ", t)

    # from original to the rest:

    elif fr == "original" and to == "tera":
        t = f * 10 ** -12
        print("The number = ", t)
    elif fr == "original" and to == "giga":
        t = f * 10 ** -9
        print("The number = ", t)
    elif fr == "original" and to == "mega":
        t = f * 10 ** -6
        print("The number = ", t)
    elif fr == "original" and to == "kilo":
        t = f * 10 ** -3
        print("The number = ", t)
    elif fr == "original" and to == "centi":
        t = f * 10 ** 2
        print("The number = ", t)
    elif fr == "original" and to == "milli":
        t = f * 10 ** 3
        print("The number = ", t)
    elif fr == "original" and to == "micro":
        t = f * 10 ** 6
        print("The number = ", t)
    elif fr == "original" and to == "nano":
        t = f * 10 ** 9
        print("The number = ", t)
    elif fr == "original" and to == "picro":
        t = f * 10 ** 12
        print("The number = ", t)

    # from centi to the rest:

    elif fr == "centi" and to == "tera":
        t = f * 10 ** -14
        print("The number = ", t)
    elif fr == "centi" and to == "giga":
        t = f * 10 ** -11
        print("The number = ", t)
    elif fr == "centi" and to == "mega":
        t = f * 10 ** -8
        print("The number = ", t)
    elif fr == "centi" and to == "kilo":
        t = f * 10 ** -5
        print("The number = ", t)
    elif fr == "centi" and to == "original":
        t = f * 10 ** -2
        print("The number = ", t)
    elif fr == "centi" and to == "milli":
        t = f * 10
        print("The number = ", t)
    elif fr == "centi" and to == "micro":
        t = f * 10 ** 4
        print("The number = ", t)
    elif fr == "centi" and to == "nano":
        t = f * 10 ** 7
        print("The number = ", t)
    elif fr == "centi" and to == "picro":
        t = f * 10 ** 10
        print("The number = ", t)

    # from milli to the rest:

    elif fr == "milli" and to == "tera":
        t = f * 10 ** -15
        print("The number = ", t)
    elif fr == "milli" and to == "giga":
        t = f * 10 ** -12
        print("The number = ", t)
    elif fr == "milli" and to == "mega":
        t = f * 10 ** -9
        print("The number = ", t)
    elif fr == "milli" and to == "kilo":
        t = f * 10 ** -6
        print("The number = ", t)
    elif fr == "milli" and to == "original":
        t = f * 10 ** -3
        print("The number = ", t)
    elif fr == "milli" and to == "centi":
        t = f * 10 ** -1
        print("The number = ", t)
    elif fr == "milli" and to == "micro":
        t = f * 10 ** 3
        print("The number = ", t)
    elif fr == "milli" and to == "nano":
        t = f * 10 ** 6
        print("The number = ", t)
    elif fr == "milli" and to == "picro":
        t = f * 10 ** 9
        print("The number = ", t)

    # from micro to the rest:

    elif fr == "micro" and to == "tera":
        t = f * 10 ** -18
        print("The number = ", t)
    elif fr == "micro" and to == "giga":
        t = f * 10 ** -15
        print("The number = ", t)
    elif fr == "micro" and to == "mega":
        t = f * 10 ** -12
        print("The number = ", t)
    elif fr == "micro" and to == "kilo":
        t = f * 10 ** -9
        print("The number = ", t)
    elif fr == "micro" and to == "original":
        t = f * 10 ** -6
        print("The number = ", t)
    elif fr == "micro" and to == "centi":
        t = f * 10 ** -4
        print("The number = ", t)
    elif fr == "micro" and to == "milli":
        t = f * 10 ** -3
        print("The number = ", t)
    elif fr == "micro" and to == "nano":
        t = f * 10 ** 3
        print("The number = ", t)
    elif fr == "micro" and to == "picro":
        t = f * 10 ** 6
        print("The number = ", t)

    # from nano to the rest:

    elif fr == "nano" and to == "tera":
        t = f * 10 ** -21
        print("The number = ", t)
    elif fr == "nano" and to == "giga":
        t = f * 10 ** -18
        print("The number = ", t)
    elif fr == "nano" and to == "mega":
        t = f * 10 ** -15
        print("The number = ", t)
    elif fr == "nano" and to == "kilo":
        t = f * 10 ** -12
        print("The number = ", t)
    elif fr == "nano" and to == "original":
        t = f * 10 ** -9
        print("The number = ", t)
    elif fr == "nano" and to == "centi":
        t = f * 10 ** -7
        print("The number = ", t)
    elif fr == "nano" and to == "milli":
        t = f * 10 ** -6
        print("The number = ", t)
    elif fr == "nano" and to == "micro":
        t = f * 10 ** -3
        print("The number = ", t)
    elif fr == "nano" and to == "picro":
        t = f * 10 ** 3
        print("The number = ", t)

    # from picro to the rest:

    elif fr == "picro" and to == "tera":
        t = f * 10 ** -24
        print("The number = ", t)
    elif fr == "picro" and to == "giga":
        t = f * 10 ** -21
        print("The number = ", t)
    elif fr == "picro" and to == "mega":
        t = f * 10 ** -18
        print("The number = ", t)
    elif fr == "picro" and to == "kilo":
        t = f * 10 ** -15
        print("The number = ", t)
    elif fr == "picro" and to == "original":
        t = f * 10 ** -12
        print("The number = ", t)
    elif fr == "picro" and to == "centi":
        t = f * 10 ** -10
        print("The number = ", t)
    elif fr == "picro" and to == "milli":
        t = f * 10 ** -9
        print("The number = ", t)
    elif fr == "picro" and to == "micro":
        t = f * 10 ** -6
        print("The number = ", t)
    elif fr == "picro" and to == "nano":
        t = f * 10 ** -3
        print("The number = ", t)
    else:
        print("sorry can't help you with that 😞")


def time_converter():
    print("press 1 Convert hours, minutes, seconds to seconds")
    print("press 2 Convert seconds to hours, minutes, seconds")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))

        total_seconds = (hours * 3600) + (minutes * 60) + seconds
        print(f"The total seconds are: {total_seconds} seconds")


    elif choice == 2:
        total_seconds = int(input("Enter total seconds: "))

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        print(f"{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds")


    else:
        print("Invalid choice. Please enter 1 or 2.")


def calculate_gpa():  # function to calculate GPA          #ahmed ihab
    num_courses = int(input("Enter the number of courses: "))

    total_credits = 0
    total_grade_points = 0
    for x in range(num_courses):
        course_name = input("Enter the name of the course: ")
        credits = int(input("Enter the number of credits for {}: ".format(course_name)))
        grade = input("Enter the grade (A, B, C, D, F) for {}: ".format(course_name))

        if grade == 'A':
            grade_points = 4.0
        elif grade == 'B':
            grade_points = 3.0
        elif grade == 'C':
            grade_points = 2.0
        elif grade == 'D':
            grade_points = 1.0
        elif grade == 'F':
            grade_points = 0.0
        else:
            print("Invalid grade entered. Please enter A, B, C, D, or F.")
            return

        course_gpa = grade_points * credits
        total_grade_points += course_gpa
        total_credits += credits
        if total_credits == 0:
            print("Error: Total credits cannot be zero.")
            return
        gpa = total_grade_points / total_credits
        print("\nOverall GPA: {:.2f}".format(gpa))


def current_intensity_finder(v, r):  # function to calculate current intensity
    current_intensity = v / r
    return current_intensity


def dist():  # function to calculate distance
    S = int(input("What is the value of speed? "))
    T = int(input("What is the value of time? "))
    dist = S * T
    print("The value of distance is ", dist)
    return dist


import datetime
from playsound import playsound


def alarm():
    alhr = int(input("enter the hour: "))
    almin = int(input("enter the minutes: "))
    a_p_m = input("am/pm: ")
    if a_p_m == "pm":
        alhr += 12
    while True:
        if alhr == datetime.datetime.now().hour and almin == datetime.datetime.now().minute:
            print("Sound On... ")
            playsound("E:\\python project\\HighwaytoHell-[AudioTrimmer.com].wav")
            break


import time
from playsound import playsound


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("TIME'S UP!")
    playsound("E:\\python project\\Alarm01.wav")



