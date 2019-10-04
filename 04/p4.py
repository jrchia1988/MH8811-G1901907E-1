#C1
c_list=[9,41,12,3,74,15]
min_value=c_list[0]
for i in range(1,len(c_list)):
    if c_list[i]<min_value:
        min_value=c_list[i]
print(min_value)

#C2
def min_(ls):
    min_value=ls[0]
    for i in range(1,len(ls)):    
        if ls[i]<min_value:
            min_value=ls[i]
    print(min_value)
    
def max_(ls):
    max_value=ls[0]
    for i in range(1,len(ls)):
        if ls[i]>max_value:
            max_value=ls[i]
    print(max_value)
    
def average(ls):
    total_sum=0
    for i in range(len(ls)):
        total_sum+=i
    average_value=total_sum/len(ls)
    print(average_value)
    
def median(ls):
    ls=sorted(ls)
    if len(ls)%2==0:
          i=int(len(ls)/2)
          median_value=(ls[i]+ls[i+1])/2
    else:
          i=(len(ls)+1)/2
          median_value=ls[i]
    print(median_value)
    
def range_(ls):
    print(max(ls)-min(ls))
    
min_(c1_list)
max_(c1_list)
average(c1_list)
median(c1_list)
range_(c1_list)

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

average(lines)
min_(lines)
max_(lines)
median(lines)
range_(lines)

#Homework
def sample_variance(ls):
    total_sum=0
    mean=average(ls)
    for i in ls:
        total_sum+=(i-mean)**2
    variance=total_sum/len(ls)-1
    print(variance)

sample_variance(lines)
    
