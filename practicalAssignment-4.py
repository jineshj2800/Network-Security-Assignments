import math
import statistics

print("The formula is: X(k+1) = a * Xk + c mod m")
seed_num = 12
multiplier = 3
increment = 3
modulus = 5
unit = 100

# linear congruent generator
def lcg():
    lcg_random = []
    num_base = seed_num
    for i in range(unit, 0, -1):
        rd = (multiplier * num_base + increment) % modulus
#         print(rd)
        lcg_random.append(rd)
        num_base = rd
        
    return lcg_random

lcg_random = lcg()

import sys

j = 7
k = 10
modval = 5

seed = "155785692479641"

unit = 100

def strtodigit(val):
    arr = []
    for i in range(len(val)):
        arr.append(int(val[i]))
    return arr


s = strtodigit(seed)


def laggedfibgen():
    slen = len(s)
    lfg = []
    for n in range(1000):
        out = (s[slen - j-1] + s[slen - k - 1]) % modval
        for i in range(len(s)-1):
            s[i] = s[i+1] 
        s[slen-1] = out
        lfg.append(out)
    return lfg

lfg_random = laggedfibgen()

#runs test of randomness
def runsTest(l, l_median):
  
    runs, n1, n2 = 0, 0, 0
      
    # Checking for start of new run
    for i in range(len(l)):
          
        # no. of runs
        if (l[i] >= l_median and l[i-1] < l_median) or \
                (l[i] < l_median and l[i-1] >= l_median):
            runs += 1  
          
        # no. of positive values
        if(l[i]) >= l_median:
            n1 += 1   
          
        # no. of negative values
        else:
            n2 += 1   
  
    runs_exp = ((2*n1*n2)/(n1+n2))+1
    stan_dev = math.sqrt((2*n1*n2*(2*n1*n2-n1-n2))/ \
                       (((n1+n2)**2)*(n1+n2-1)))
  
    z = (runs-runs_exp)/stan_dev
  
    return z

"""(Zcritical =1.96 for confidence level of 95%) . 
The null hypothesis is rejected i.e. the numbers are 
declared not to be random, if |Z|>Zcritical . """
lfg_random = [float(i)/max(lfg_random) for i in lfg_random]
lcg_random = [float(i)/max(lcg_random) for i in lcg_random]
l_median= statistics.median(lfg_random)
Z = abs(runsTest(lfg_random, l_median))
print("Zcritical = 1.96")
print('Lagged fib random number Z-statistic = ', Z)

l_median= statistics.median(lcg_random)
Z = abs(runsTest(lcg_random, l_median))
print('linear congruent generator random number Z-statistic = ', Z)

def kstest1(arr_1):
    arr_1 = [float(i)/max(arr_1) for i in arr_1]
    from scipy.stats import kstest
    x = kstest(arr_1, "uniform")
#     print(x)
    return x

Z = kstest1(lfg_random)
# print("D 95% confifdence critical = ", 1.36/10)
print('Lagged fib gen = ', Z)

Z = kstest1(lcg_random)
print('linear congruent generator ', Z)
