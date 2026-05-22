import math

#LEVEL1
empty_list = list()

list_example = [1,2,3,4,5,6]

print(len(list_example))

first_item = list_example[0]
last_item = list_example[-1]
middle_item = list_example[math.floor((len(list_example)-1)/2)]

print(f"first: {first_item}; middle: {middle_item}; last: {last_item}")

mixed_data_types = ['Kacper', 21, 1.71, 'married', {'city': 'Poznan', 'voivode': 'Wielkopolska'}]

it_companies = list(['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'])

print(it_companies)

print(len(it_companies))

print(it_companies[0])
print(it_companies[math.floor((len(it_companies)-1)/2)])
print(it_companies[-1])

it_companies[0] = 'Meta'

print(it_companies)

it_companies.append('Nintendo')

print(it_companies)

it_companies.insert(-1, 'Sega')

print(it_companies)

it_companies[0] = it_companies[0].upper()

print(it_companies)

joined_it_companies = '#; '.join(it_companies)
print(joined_it_companies)

print('Apple' in it_companies)

it_companies.sort()

print(it_companies)

it_companies.reverse()

print(it_companies)

first_three_companies = it_companies[:3]
last_three_companies = it_companies[-3:]
middle_companies = it_companies[3:-3]

print(first_three_companies)
print(middle_companies)
print(last_three_companies)

del it_companies[0]
del it_companies[3]
del it_companies[-1]

it_companies.clear()
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)

print(front_end)

full_stack = front_end.copy()

redux_index = full_stack.index('Redux')

full_stack.insert(redux_index+1, 'Python')
full_stack.insert(redux_index+2, 'SQL')

print(full_stack)

#LEVEL2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
max_age = max(ages)
min_age = min(ages)

ages.append(max_age)
ages.append(min_age)

median = 0 
ages.sort()

mid = len(ages) // 2
if ages % 2 == 0:
    median = (ages[mid-1] + ages[mid]) / 2
else:
    median = ages[mid]

print(median)

average = sum(ages)/len(ages)

print(max_age - min_age)

print(abs(min_age - average) == abs(max_age - average))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

middle_country = []

if len(countries) % 2 == 0:
    middle_country.append(countries[int(len(countries)/2)-1])
    middle_country.append(countries[int(len(countries)/2)])
else:
    middle_country.append(countries[len(countries)//2])

print(middle_country)

mid = (len(countries) + 1) // 2
first_part = countries[:mid]
second_part = countries[mid:]

countries_example = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

china, russia, usa, *scandic_countries = countries_example

