import numpy as np
import csv
import matplotlib.pyplot as plt
# in the next 4 lines ,we initialize matrices for all records to add values in them
TV=[]
Radio=[]
NewsPaper=[]
Sales=[]


with open('Advertising.csv', newline='') as csvfile:
    file_reader = csv.reader(csvfile, delimiter=',')
    headers= next(file_reader)
    # in the next 4 lines , we put data in the initialized matrices above
    for column in file_reader:
        TV.append(float(column[1]))
        Radio.append(float(column[2]))
        NewsPaper.append(float(column[3]))
        Sales.append(float(column[4]))
plt.subplot(3,1,1)
plt.plot(TV,Sales,'.')
plt.title('TV-Sales')
plt.xlabel(headers[1])
plt.ylabel(headers[4])
plt.axis('equal')
plt.subplot(3,1,2)
plt.plot(TV,Sales,'.')
plt.title('Radio-Sales')
plt.xlabel(headers[2])
plt.ylabel(headers[4])
plt.axis('equal')
plt.subplot(3,1,3)
plt.plot(TV,Sales,'.')
plt.title('NewsPaper-Sales')
plt.xlabel(headers[3])
plt.ylabel(headers[4])
plt.axis('equal')
plt.show()
