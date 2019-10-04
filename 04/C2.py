def min(ls):
    for i in range(1,len(ls)):
        if ls[i]<ls[i-1]
            min_value=ls[i]
        else:
            min_value=ls[i-1]
    return min_value
    
def max(ls):
    for i in range(1,len(ls)):
        if ls[i]>ls[i-1]
            max_value=ls[i]
        else:
            max_value=ls[i-1]
    return max_value
    
def average(ls):
    sum=0
    for i in range(len(ls)):
        total_sum+=i
    average_value=total_sum/len(ls)
    return average_value
    
def median(ls):
    if len(ls)%2==0:
          i=len(ls)/2
          median_value=(ls[i]+ls[i+1])/2
    else:
          i=(len(ls)+1)/2
          median_value=ls[i]
    return median_value
    
def range(ls):
    return max(ls)-min(ls)
    
c1_list=[9,41,12,3,74,15]

min(c1_list)
max(c1_list)
average(c1_list)
median(c1_list)
range(c1_list)
        
