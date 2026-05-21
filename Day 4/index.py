import math

strings = ['Thirty', 'Days', 'of', 'Python']
sentence = ' '.join(strings)
print(sentence)

strings = ['Coding', 'For', 'All']
company = ' '.join(strings)
print(company)

print(len(company))

upper_company = company.upper()
print(upper_company)

lower_company = company.lower()
print(lower_company)

capitalize_company = company.capitalize()
print(capitalize_company)

title_company = company.title()
print(title_company)

swapcase_company = company.swapcase()
print(swapcase_company)

first_word = company[0:6]
print(first_word)

if(company.find('Coding')!=-1):
    print("substring found")

replace_company = company.replace('Coding', 'Python')
print(replace_company)

sentence = 'Python for Everyone'
sentence = sentence.replace('Everyone', 'All')
print(sentence)

sentence = 'Coding for All'
words = sentence.split(" ")

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(',')
companies = list(map(str.lstrip, companies))
print(companies)

print(sentence[0])
print(len(sentence)-1)
print(sentence[10])

def create_acronym(sentence: str) -> str:
    words = sentence.split(' ')
    acronym = ''
    for word in words:
        acronym += word[0]

    return acronym

sentence = 'Python For Everyone'

print(create_acronym(sentence))
print(create_acronym('Coding For Everyone'))

sentence = 'Coding For All'
print(sentence.index('C'))
print(sentence.index('F'))
sentence = 'Coding For All People'
print(sentence.rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
l =sentence.find('because')
r =sentence.rfind('because')

print(sentence[l:r+len('because')])
print(sentence.find('because'))

sentence = 'Coding For All'
print(sentence.startswith('Coding'))
print(sentence.endswith('coding'))

sentence = '   Coding For All      '.strip()
print(sentence)

sentence_1 = '30DaysOfPython'
sentence_2 = 'thirty_days_of_python'
print(sentence_1.isidentifier())
print(sentence_2.isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

radius = 10
area = math.pi*radius**2
print(f"The area of a circle with radius {radius} is {area} meters square.")

a = 8
b = 6
total = a+b
sub = a-b
multiplication = a*b
division = a / b
remainder = a%b
floor_division = a // b
power = a**b
print(f'''{a} + {b} = {total}
{a} - {b} = {sub}
{a} * {b} = {multiplication}
{a} / {b} = {division}
{a} % {b} = {remainder}
{a} // {b} = {floor_division}
{a} ** {b} = {power}''')