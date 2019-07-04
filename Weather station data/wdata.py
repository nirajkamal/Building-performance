import pandas
import csv
import numpy
import math

data = pandas.read_csv('input.csv')
index = list(data)
time = list(data['date and time'])
data = numpy.array(data)
newdata =[]
newdata.append(index[2:])
n=0
rowlength = len(index)-2
sum = [0] * rowlength
newdata2 = []
newdata2.append(index[2:])
currenthr = 13
hour =13
switch = 0
for t in time:
    ti = t.split(' ')
    date = ti[0]
    ti = ti[1]
    minute = int(ti.split(':')[1])
    i = time.index(t)
    rowlength = len(index)
    adder = data[i][2:rowlength]
    rowlength = len(index)-2
    sum = numpy.add(sum,adder)
    currenthr = hour
    hour =  int(ti.split(':')[0])
    if currenthr != hour:
      if switch == 1:
        average = sum/n
        average = numpy.append(average,hour)
        average = numpy.append(average,date)
        n=0
        newdata.append(average)
        sum = [0] * rowlength
        sum = numpy.add(sum, adder)
    if currenthr != hour:
        adder = numpy.append(adder, date)
        adder = numpy.append(adder, ti)
        newdata2.append(adder)
    n = n+1
    switch = 1

with open('output.csv','w', newline='') as fp:
        wr = csv.writer(fp,dialect = 'excel')
        wr.writerows (newdata)

with open('output2.csv', 'w', newline='') as fp:
    wr = csv.writer(fp, dialect='excel')
    wr.writerows(newdata2)
