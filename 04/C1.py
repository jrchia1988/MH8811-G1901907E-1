min_list=[9,41,12,3,74,15]
for i in range(1,len(min_list)):
    if min_list[i]<min_list[i-1]:
        min_value=min_list[i]
    else:
        min_value=min_list[i-1]
print(min_value)
        
  
  
