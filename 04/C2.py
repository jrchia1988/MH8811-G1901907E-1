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
    
c1_list=[9,41,12,3,74,15]

min_(c1_list)
max_(c1_list)
average(c1_list)
median(c1_list)
range_(c1_list)
        
