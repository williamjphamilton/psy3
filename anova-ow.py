import scipy
from scipy import stats # has the f-tables 

dva = [4, 4, 5, 6, 6]
dvb = [4, 5, 7, 7, 7]
dvc = [3, 4, 4, 4, 5]
v_all = []
v_all.extend(dva)
v_all.extend(dvb)
v_all.extend(dvc)

def Average (lst):
    return sum(lst) / len(lst)

#We calculate average of all values. Then we deduct that average from each observed value
#Then we square it. This gives us the total variance.

def SST(lst):
    squares = []
    avg = Average(lst)
    for x in lst:
        squares.append((x-avg)**2)
       
    return sum(squares)

# takes in all conditions
# we need to test if all are the same length
def SSB(lst):
    sums = []
    for x in lst: 
        sums.append((Average(x) - Average(v_all))**2)
    return sum(sums) * len(lst[0]) 

#take the average of each dv-group and subtract from value in each group
#sum the averages
def SSW(lst):
    sums = []
    for x in lst:
        avg = Average(x)
        for y in x:
            sums.append((y-avg)**2)
    return sum(sums)

dva_barx = Average(dva)
dvb_barx = Average(dvb)
dvc_barx = Average(dvc)

sst = SST(v_all)
ssb = SSB([dva,dvb,dvc])
ssw = SSW([dva,dvb,dvc])

# control that SST = SSB + SSW

# calculate degrees of freedom 
dfb = 2
msb = ssb / dfb

dfw = 3*(len(dva)-1) 
msw = ssw / dfw

f = msb/msw

eta2 = ssb / sst

# we find the critical f-value in python
fcrit = scipy.stats.f.ppf(1-.05,dfb,dfw)
print (fcrit)


