import pandas
import csv
import numpy
import psySI as SI
import math
import comodel as como
data = pandas.read_csv('input.csv')
#input imported as data
l = len(data)-2
days = int(l/24)
index = list(data)
post = []
post2 = []
row = []
row.append('Date and Time')
for s in index:
    if index.index(s)>0:
      k = index.index(s)
      row.append(s + '(max)')
      row.append(s + '(maxtime)')
      row.append(s+'(min)')
      row.append(s+'(mintime)')
      row.append( s+'(mean)')
#first row of output.csv

Wl_1Fac = list(data['Wl-1Facing'])
Wl_1Fac = Wl_1Fac[0]
Wl_2Fac = list(data['Wl-2Facing'])
Wl_2Fac = Wl_2Fac[0]

post.append(row)   
for i in range(days):
    j = (i*24) + 1
    row = []
    row2 =[]
    for s in index:
        split = data[s][j:j+24]
        splitdate = list(data['Date and Time'][j:j+24])
        if (s=='Date and Time'):
            row.append(data[s][j])
        else:
            k = index.index(s)
            split = list(split)
            maxi = max(split)
            try:
             timemax = splitdate[split.index(maxi)].split( )[1]
            except:
             timemax = 'nan'
            mini = min(split)
            try:
             timemin = splitdate[split.index(mini)].split( )[1]
            except:
             timemin = 'nan'
            try:
             mean = numpy.mean(split)
            except:
             mean = 'nan'
            row.append(maxi)
            row.append(timemax)
            row.append(mini)
            row.append(timemin)
            row.append(mean)
            if (s== 'TA in'):
                TA_in_max = maxi
                TA_in_min = mini
                TA_in_maxtim = timemax
                TA_in_mintim = timemin
                print( s + ' defined')
            if (s== 'TA out'):
                TA_out_max = maxi
                TA_out_min = mini
                TA_out_maxtim = timemax
                TA_out_mintim = timemin
                print( s + ' defined')
            if (s== 'TWl-1 in'):
                TWl_1_in_max = maxi
                TWl_1_in_min = mini
                TWl_1_in_maxtim = timemax
                TWl_1_in_mintim = timemin
                print( s + ' defined')
            if (s== 'TWl-1 out'):
                TWl_1_out_max = maxi
                TWl_1_out_min = mini
                TWl_1_out_maxtim = timemax
                TWl_1_out_mintim = timemin
                print( s + ' defined')
            if (s== 'TWl-2 in'):
                TWl_2_in_max = maxi
                TWl_2_in_min = mini
                TWl_2_in_maxtim = timemax
                TWl_2_in_mintim = timemin
                print( s + ' defined')
            if (s== 'TWl-2 out'):
                TWl_2_out_max = maxi
                TWl_2_out_min = mini
                TWl_2_out_maxtim = timemax
                TWl_2_out_mintim = timemin
                print( s + ' defined')
            if (s== 'TRf in'):
                TRf_in_max = maxi
                TRf_in_min = mini
                TRf_in_maxtim = timemin
                TRf_in_mintim = timemax
                print( s + ' defined')
            if (s== 'TRf out'):
                TRf_out_max = maxi
                TRf_out_min = mini
                TRf_out_maxtim = timemax
                TRf_out_mintim = timemin
                print( s + ' defined')
    post.append(row)
    if (Wl_1Fac == 'W'):
        Corr_1= 0.75
    if (Wl_1Fac == 'E'):
        Corr_1 = 0.63
    if (Wl_1Fac == 'S'):
        Corr_1 = 0.42
    if (Wl_1Fac == 'N'):
        Corr_1 = 0.34
    if (Wl_2Fac == 'W'):
        Corr_2= 0.75
    if (Wl_2Fac == 'E'):
        Corr_2 = 0.63
    if (Wl_2Fac == 'S'):
        Corr_2 = 0.42
    if (Wl_2Fac == 'N'):
        Corr_2 = 0.34
    try:
     TPI_1 = ((((TWl_1_in_max - 30)*100)/8))
     CTPI_1 = ((TPI_1)-50) * Corr_1 + 50
    except:
        print('Wl-1 not defined')
    try:
     TPI_2 = ((((TWl_2_in_max - 30)*100)/8))
     CTPI_2 = ((TPI_2)-50) * Corr_2 + 50
    except:
        print('Wl-2 not defined')
    try:
     TPI_r = ((((TRf_in_max - 30)*100)/8))
     CTPI_r = ((TPI_r)-50) * 0.92 + 50
    except:
        print('roof not defined')
    try:
     Depreciation_factor = (TA_in_max - TA_in_min) / (TA_out_max - TA_out_min)
     Damping_Percentage = (1 - Depreciation_factor) * 100
     Max_Damping_day = TA_out_max - TA_in_max
     Max_Damping_night = TA_in_min - TA_out_min
     Time_lag_day =  int(TA_in_maxtim.split(':')[0])- int(TA_out_maxtim.split(':')[0])
     Time_lag_night = int(TA_in_mintim.split(':')[0]) - int(TA_in_mintim.split(':')[0])
    except:
        print('see all the values for TA')
    row2=[]
    row2.append(CTPI_1)
    row2.append(CTPI_2)
    row2.append(CTPI_r)
    row2.append(Depreciation_factor)
    row2.append(Max_Damping_day)
    row2.append(Max_Damping_night)
    row2.append(Time_lag_day)
    row2.append(Time_lag_night)
    post2.append(row2)

with open("result/output.csv", "a") as fp:
    wr = csv.writer(fp, dialect='excel')
    for i in post:
        wr.writerow(i)


        
with open("result/performance-daily.csv", "a") as fp:
    wr = csv.writer(fp, dialect='excel')
    for i in post2:
        wr.writerow(i)

        
        
comf = pandas.read_csv('bin/comf.csv')
awarm = pandas.read_csv('bin/accwarm.csv')
comb = pandas.read_csv('bin/combine.csv')
templ = pandas.read_csv('bin/tempcomb.csv')
hum = list(comf)
hum2 = list(awarm)
comf = numpy.array(comf)
awarm = numpy.array(awarm)
comb = numpy.array(comb)
templ = numpy.array(templ)
time = list(data['Date and Time'])
tin = list(data['TA in'])
rhin = list(data['RH in'])
clo = list(data['Clo '])
clo = float(clo[0])
postcomf =[]
row = ['Date','Time','inttime','Comfort m/s','Acceptibly warm m/s','Mixed m/s','Temp','Rh','tw','TSI','PMV','PPD','Standrd Eff Temp','TA adj','Cool effect']
postcomf.append(row)
vco = 0
co = 0
aw = 0
unc = 0
count = 0
for t in time:
  if time.index(t)>0:
    d = time.index(t)
    t = t.split( )
    temp = tin[d]
    if temp>0:
     if (temp - int(temp)) >0.5:
        temp2 = int(temp+1)
     else:
        temp2 = int(temp)
    rh = rhin[d]
    if rh>0:
     if (rh - 10*(int(int(rh)/10))) > 5:
        rh2 = 10*(int(int(rh)/10))+10
     else:
        rh2 = 10*(int(int(rh)/10))
    row = []
    b = 0
    while temp2>comf[b][0] :
            b = b+1
    c = 1
    while rh2>int(hum[c]):
            c = c+1
    d=0
    while temp2>awarm[d][0]:
        d=d+1
    e=1
    while rh2>int(hum2[e]):
        e=e+1
    if comb[d][e] == 0:
        vco = vco+1
    if comb[d][e] == 1:
        co = co+1
    if comb[d][e] == 2:
        aw = aw+1
    if comb[d][e] == 3:
        unc = unc +1
    warcom = max (float(comf[b][c]),float(awarm[d][e]))
    if (comf[b][c]<=0) & (awarm[d][e]>=0):
        warcom = 3
    s = SI.state("DBT",(273+temp),"RH",(rh/100),101325)
    try:
      tw = s[5] - 273
    except TypeError:
        tw = s[5]
    try:
      TSI = (0.308*tw) + (0.745*temp) - (2.06*(math.sqrt((0.9*warcom)+0.841)))
    except:
        TSI = None
    
    tiime = t[1].split(':')
 #   if (int(tiime[0])>7 & int(tiime[0])<23):
 #     Met = 1.7
    #else:
    #      Met =0.7
    Met = 1.5
    try: 
       model= como.comfPMVElevatedAirspeed(temp,temp,(0.3),rh/100,Met,clo,0)
    except:
        model = [0,0,0,0,0,0,0]
    templ[d][e] = templ[d][e]+1
    count = count +1
    row.append(t[0])
    row.append(t[1])
    row.append(int(tiime[0]))
    row.append(comf[b][c])
    row.append(awarm[d][e])
    row.append(warcom)
    row.append(temp)
    #row.append(comf[b][0])
    #row.append(awarm[d][0])
    #row.append(hum[c])
    #row.append(hum2[c])
    row.append(rh)
    row.append(tw)
    row.append(TSI)
    row.append(model[0])
    row.append(model[1])
    row.append(model[2])
    row.append(model[3])
    row.append(model[4])
    postcomf.append(row)   

postcomf.append([vco,co,aw,unc])
with open("result/comfort.csv", "a") as fp:
    wr = csv.writer(fp, dialect='excel')
    for i in postcomf:
        wr.writerow(i)

templ = (templ/count)*100

template = [hum2]
for i in templ:
    template.append(i)


with open("result/distribution.csv",'w') as fp:
    wr = csv.writer(fp,dialect = 'excel')
    wr.writerows (template)
