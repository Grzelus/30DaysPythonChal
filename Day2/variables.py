import math

#level 1

#Day2: 30 Days of python programming
first_name = 'Kacper'
last_name = 'Grzelak'
full_name = f"{first_name} {last_name}"
country = 'Poland'
city = 'Poznan'
age = 21
year = 2026
is_married = False
is_true = False
is_light_on = True
eye_color, hair_color = 'blue', 'blonde'

data = [first_name, last_name, full_name, country,city,age,year,is_married,is_true,is_light_on, eye_color, hair_color]

#level 2

for d in data:
    print(type(d))

print(len(first_name))

print(len(first_name) == len(last_name))

num_one, num_two = 5, 4

total = num_one + num_two

diff = num_one - num_two

product = num_one * num_two

division = num_one / num_two

remainder = num_two % num_one

exp = num_one ** num_two

floor_division = num_one // num_two

radius = 30

def calculate_circle_area(radius: int):
    return radius**2*math.pi

def calculate_circle_circumference(radius: int):
    return 2*math.pi*radius

area_of_circle = calculate_circle_area(radius)

circum_of_circle = calculate_circle_circumference(radius)

user_radius = int(input("Enter radius:"))

print(calculate_circle_area(user_radius))

user_first_name = input("Enter first name:")
user_last_name = input("Enter last name:")
user_country = input("Enter country:")
user_age = int(input("Enter age:"))
