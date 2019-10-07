#C1
c_list=[9,41,12,3,74,15]
min_value=None
for i in c_list:
    if min_value==None:
        min_value=i
        continue
    if i<min_value:
        min_value=i
print(min_value)

#C2
def my_min(ls):
    min_value=None
    for i in ls:
        if min_value==None:
            min_value=i
            continue
        if i<min_value:
            min_value=i
    return min_value
    
def my_max(ls):
    max_value=None
    for i in ls:
        if max_value==None:
            max_value=i
            continue
        if i>max_value:
            max_value=i
    return max_value
    
def my_average(ls):
    total_sum=0
    for i in ls:
        total_sum+=i
    average_value=total_sum/len(ls)
    return average_value
    
def my_median(ls):
    ls.sort()
    if len(ls)%2==0:
          i=int(len(ls)/2)
          median_value=(ls[i]+ls[i-1])/2
    else:
          i=(len(ls)+1)/2
          median_value=ls[i]
    return median_value

def my_range(ls):
    range_value=my_max(ls)-my_min(ls)
    return range_value
    
print('Min: ',my_min(c1_list))
print('Max: ',my_max(c1_list))
print('Average :',my_average(c1_list))
print('Median: ',my_median(c1_list))
print('Range: ',my_range(c1_list))

#C3
def getFileLines(fname):
      fhandle=open(fname)
      lines=[]
      for line in fhandle:
            line=line.rstrip()
            if line:
                  lines.append(line)
      fhandle.close()
      return lines
      
lines=getFileLines('MH8811-04-Data.csv')

print('Average: ',my_average(lines))
print('Min: ',my_min(lines))
print('Max: ',my_max(lines))
print('Median: ',my_median(lines))
print('Range: ',my_range(lines))

#Homework
def sample_variance(ls):
    total_sum=0
    mean=my_average(ls)
    for i in ls:
        total_sum+=(i-mean)**2
    variance=total_sum/(len(ls)-1)
    return variance

print('Sample Variance: ',sample_variance(lines))
    
