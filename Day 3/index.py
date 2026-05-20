import math

age = 21
height = 1.72
number = 1-1j

def calculate_triangle_area(b: int, h: int):
    return b*h/2

base = int(input("Enter base:"))
height = int(input("Enter height: "))

print(f"The area of the triangle is {calculate_triangle_area(base, height)}")

def my_own_sum(*args: int):
    total = 0
    for number in args:
        total += number
    
    return total

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

print(f"The perimeter of the triangle is {my_own_sum(a,b,c)}")

def calculate_area_and_perimeter_of_rectangle(a:int, b:int):
    area = a*b
    perimeter = 2*(a+b)

    return area, perimeter

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))

area, perimeter = calculate_area_and_perimeter_of_rectangle(a, b)

print(f"Area: {area}; Perimeter: {perimeter}")

def calculate_area_and_circumference_of_circle(radius: int):
    area = math.pi*radius**2
    circumference = 2*math.pi*radius

    return area, circumference

radius = int(input("Enter radius: "))

area, circumference = calculate_area_and_circumference_of_circle(radius)

print(f"Area: {area}; Circumference: {circumference}")

a = int(input("Enter a of the linear function: "))
b = int(input("Enter b of the linear function: "))

x = -b/a


print(f"slope: {a}; X-intercept: {x}; Y-intercept: {b}" )

slope = (2-10)/(2-6)
euclidean_distance = math.sqrt((2-6)**2 + (2-10)**2)

print(f"slope: {slope}; euclidean_distance: {euclidean_distance}")

print(slope == a)

def calculate_roots(a: int, b:int, c:int):
    delta = b**2 - 4*a*c
    return (-b + math.sqrt(delta)) / (2*a), (-b - math.sqrt(delta)) / (2*a)

a = 1
b = 6
c = 9

print(calculate_roots(a,b,c))

print(len('python'), len('dragon'))

print('python' is 'dragon')

sentence = " hope this course is not full of jargon"

print('jargon' in sentence)

print('on' not in 'dragon' and 'on' not in 'python')

print(str(float(len('ptyhon'))))

def is_odd(number: int):
    return number % 2

result = 7//3

print(result == int(2.7))

print(type('10') is type(10))

print(int('9.8') == 10)

def calculate_earning(hours: int, rate: int):
    return hours*rate

hours = int(input("Enter hours: "))
rate = int(input("Enter rate: "))

print(f"Your weekly earning is {calculate_earning(hours, rate)}")

def seconds_of_your_life(years: int):
    if years > 100:
        print("You passed away!")
        return None
    
    return years*365*24*60**2

years_lived = int(input("Enter number of years you have lived: "))
print(f"You have lived for {seconds_of_your_life} seconds.")

def multiply(number: int):
    result = []
    result.append(number)
    for i in range(4):
        result.append(number**i)

    return result

for i in range(1, 6):
    row = multiply(i)
    for j in range(len(row)):
        print(row[j], end=" ")
    print('')

