def sample_variance(ls):
    total_sum=0
    mean=average(ls)
    for i in ls:
        total_sum+=(i-mean)**2
    variance=total_sum/len(ls)-1
    print(variance)
    
from C3 import getFileLines

lines=getFileLines('MH8811-04-Data.csv')

sample_variance(lines)
    
