import numpy as np
import csv
# in the next 4 lines ,we initialize matrices for all records to add values in them
TV=[]
Radio=[]
NewsPaper=[]
Sales=[]

file_path='Advertising.csv'
with open(file_path, newline='') as csvfile:
    file_reader = csv.reader(csvfile, delimiter=',')
    headers= next(file_reader)
    # in the next 4 lines , we put data in the initialized matrices above
    for column in file_reader:
        TV.append(float(column[1]))
        Radio.append(float(column[2]))
        NewsPaper.append(float(column[3]))
        Sales.append(float(column[4]))

Values=[TV,Radio,NewsPaper,Sales]
strings=['TV','Radio','NewsPaper','Sales']
statistics=['minimum','maximum','average','median','mean']
for i in range(5):
    print('the minimum value of  {} is '.format(strings[i]),np.amin(Values[i]))
    print('the maximum value of  {} is '.format(strings[i]),np.amax(Values[i]))
    print('the average value of  {} is '.format(strings[i]),np.average(Values[i]))
    print('the median value of  {} is '.format(strings[i]),np.median(Values[i]))
    print('the mean value of  {} is '.format(strings[i]),np.mean(Values[i]))





