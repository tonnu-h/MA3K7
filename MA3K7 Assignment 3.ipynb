# MA3K7 Assignment 3
### Due: 21 Feb 2024


#import libraries

import numpy as np
import matplotlib.pyplot as plt
import random
import seaborn as sns


## attempt 1:
##  only works up to len > 1022
array = list(range(1,2025))

while len(array)>1:
    x_a = random.choice(array)
    x_b = random.choice(array)
    
    x_new = abs(x_a-x_b)
    
    array.remove(x_a)
    array.remove(x_b)
    array.append(x_new)
    
print(x_a,x_b)


## attempt 2: working attempt
array = list(range(1,2025))

while len(array)>1:
    x_a = random.choice(array)
    array.remove(x_a)

    x_b = random.choice(array)
    array.remove(x_b)
    
    x_new = abs(x_a-x_b)
    array.append(x_new)
    
print(array)


## Producing results over many games, in this case 50.
# Producing the result, of a certain number pieces left
i=0
final_number = []
pieces_left = 1 #the '3' refers to the number of pieces left in the hat. i.e. if you want to stop when there are 2 pieces in the hat, change to '3'to '2'

while i < 50:
    array = list(range(1,2025))
    while len(array)> pieces_left:
            x_a = random.choice(array)
            array.remove(x_a)

            x_b = random.choice(array)
            array.remove(x_b)

            x_new = abs(x_a-x_b)
            array.append(x_new)
            
    final_number.append(array)
    i+=1
    
print(final_number)


# Producing the final number (above code can also do this but this one is better to be used for the proceeding visulisations)
i=0
final_number = []

while i < 100:
    array = list(range(1,2025))
    while len(array)>1:
            x_a = random.choice(array)
            array.remove(x_a)

            x_b = random.choice(array)
            array.remove(x_b)

            x_new = abs(x_a-x_b)
            array.append(x_new)
    
    #Here, we want array[0] so we can have list of numbers to plot in the next part, instead of a list of arrays
    final_number.append(array[0])
    i+=1
    
# print(final_number


# Scatter plot for the final number
plt.plot(final_number, marker='o', linestyle='none', color='powderblue')  # Plot your data

# Creating annotations for the minimum and maximum values
min_value = min(final_number)
max_value = max(final_number)
min_index = final_number.index(min_value)
max_index = final_number.index(max_value)

plt.annotate(f'Min: {min_value}', xy=(min_index, min_value), xytext=(min_index, min_value + 0.05 * (max_value - min_value)), arrowprops=dict(facecolor='red', shrink=0.05),)

plt.annotate(f'Max: {max_value}', xy=(max_index, max_value), xytext=(max_index, max_value - 0.1 * (max_value - min_value)), arrowprops=dict(facecolor='red', shrink=0.05), )

plt.xlabel('Iteration No.')
plt.ylabel('Value')
plt.title('Plot of Values of the Final Number over $1000$ games')
plt.tight_layout()
plt.show()


# Histogram to show distribution of values of final number
sns.histplot(final_number, kde=False, color='cadetblue', bins=100, edgecolor='black', line_kws={'color': 'midnightblue','lw':2})

plt.title('Histogram of Values of Final Number with Density Curve, over 1000 games')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()


# Calculating the mean and median of the value of final number over a given number of games
print(np.mean(final_number))
print(np.median(final_number))
