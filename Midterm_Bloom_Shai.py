#all imports
import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

digits = [2,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,
         9,6,0,1,3,5,6,7,8,9,10,2,3,6,8,9,10,6,7,4,3]

freq_dict = {}

for number in digits:           #creates dictionary 
    if number not in freq_dict:
        freq_dict[number] = 1
    else:
        freq_dict[number] += 1
        
for number, count in sorted(freq_dict.items()): #prints dictionary clearly
    print(f'{number:<12}{count}')

x = []
y = []

for number, count in sorted(freq_dict.items()):    #Sorts keys
    x.append(number)
    y.append(count)

x_array = np.array(x)
y_array = np.array(y)

#bar chart formating
shades = np.array(['green', 'blue', 'red', 'yellow', 'pink',
                   'black', 'orange', 'purple', 'brown',
                   'cyan', 'magenta'])    
plt.bar(x_array, y_array, color = shades)
plt.xticks(x)
plt.title('The Frequency of Different Numbers in a List')
plt.xlabel('Numbers')
plt.ylabel('Frequency')
plt.show()

change = json.dumps(freq_dict)      #python to json 

conversion = open('midtermfile.json', 'w')  #overwriting json file
conversion.write(change)
conversion.close()

conversion = open('midtermfile.json', 'r')  #reading json file
print(conversion.read())

#question 2
df = pd.read_csv('amazon-orders.csv')
print(df.head())
print(df.shape)

#cleaning
df = df.fillna(0)
print(df.head())
df['Total Charged'] = df['Total Charged'].str.replace('$','').astype(float)
df['Tax Charged'] = df['Tax Charged'].str.replace('$','').astype(float)
print(df.head())

#calculations of purchases
total = df['Total Charged'].sum()
print(total)
average = df['Total Charged'].mean()
print(average)
middle = df['Total Charged'].median()
print(middle)
largest = df['Total Charged'].max()
print(largest)
smallest = df['Total Charged'].min()
print(smallest)

#calculations of taxes
print(df['Tax Charged'].sum())
print(df['Tax Charged'].sum() / df['Total Charged'].sum())

#orders over time
df['Order Date'] = pd.to_datetime(df['Order Date'])
print(df.head())
%matplotlib inline
daily_orders = df.groupby('Order Date').sum()['Total Charged']
print(daily_orders.head())
daily_orders.plot.bar(figsize=(20,10), color='#61D199')
plt.show()

#charged graph
array_calc = np.array([0, 1, 2, 3])
array_results = np.array([average, middle, largest, smallest])
xticks = ('Mean, $47.40', 'Median, $24.27', 'Max, $953.99', 'Min, $3.69')
plt.xticks(array_calc, xticks)
plt.title('Amazon Data During the Pandemic, March 2020 to March 2021')
plt.ylabel('Dollar Amounts')
plt.bar(array_calc, array_results, color = 'purple', width = .75)
plt.grid(axis = 'y')
plt.show()
