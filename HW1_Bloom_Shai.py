favcolors = ['blue', 'black', 'green', 'purple']
print(favcolors)

numbers = list(range(30, 61, 3))
print(numbers)

weatherdict = {'sunny': 'play',
               'rainy': 'watching TV',
               'cloudy': 'walk'}
print(weatherdict)
weatherdict.update({'snowy': 'ski'})
print(weatherdict)

grade = 40
if grade >= 90:
    print('Your Grade: A')
elif grade >= 80 and grade < 90:
    print('Your Grade: B')
elif grade >= 70 and grade < 80:
    print('Your Grade: C')
else:
    print('Your Grade: F')    