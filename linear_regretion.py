import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

salesDist = pd.read_csv('./data/stores-dist.csv')
# Verify the imported data
salesDist.head()

# The district column has no relevance at this time, so it can be dropped.
salesDist = salesDist.rename(columns={'annual net sales':'sales','number of stores in district':'stores'})
salesDist.head()
# Check correlation of data prior to doing the analysis
salesDist.corr()

#sales = salesDist.drop(...)
sales = salesDist.drop(["district"], axis=1)
sales.head()

# dependent variable for y axis
y = sales['sales']
# independent variable for x axis
x = sales.stores

# Increase the size of the plot
plt.figure(figsize=(20,10))
# Create a scatter plot: Number of stores in the District vs. Annual Net Sales
plt.plot(x,y, 'o', markersize = 15)
# Add axis labels and increase the font size
plt.ylabel('Annual Net Sales', fontsize = 30)
plt.xlabel('Number of Stores in the District', fontsize = 30)
# Increase the font size on the ticks on the x and y axis
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
# Display the scatter plot
plt.show()

m, b = np.polyfit(x,y,1)
print ('The slope of line is {:.2f}.'.format(m))
print ('The y-intercept is {:.2f}.'.format(b))
print ('The best fit simple linear regression line is {:.2f}x + {:.2f}.'.format(m,
b))

y_mean = y.mean()
# x coordinate for centroid
x_mean = x.mean()
print ('The centroid for this dataset is x = {:.2f} and y = {:.2f}.'.format(x_mean
, y_mean))

# Enlarge the plot size
plt.figure(figsize=(20,10))
# Plot the scatter plot of the data set
plt.plot(x,y, 'o', markersize = 14, label = "Annual Net Sales")
# Plot the centroid point
plt.plot(x_mean,y_mean, '*', markersize = 30, color = "r")
# Plot the linear regression line
plt.plot(x, m*x + b, '-', label = 'Simple Linear Regression Line', linewidth = 4)
# Create the x and y axis labels
plt.ylabel('Annual Net Sales', fontsize = 30)
plt.xlabel('Number of Stores in District', fontsize = 30)
# Enlarge x and y tick marks
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
# Point out the centroid point in the plot
plt.annotate('Centroid', xy=(x_mean-0.1, y_mean-5), xytext=(x_mean-3, y_mean-20),
arrowprops=dict(facecolor='black', shrink=0.05), fontsize = 30)
# Create legend
plt.legend(loc = 'upper right', fontsize = 20)

def predict(query):
  if query >= 1:
    predict = m * query + b
    return predict
  else:
    print ("You must have at least 1 store in the district to predict the annual net sales.")
# Code Cell 12
# Enter the number of stores in the function to generate the net sales prediction.

print(predict(2))