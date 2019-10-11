#C1

import pickle

lst=[1,2,3,4,5]

def serialize(lst):
    string=''
    for i in lst:
        string+=i
    string='|'.join(string)
    return string
    
def deserialize(string):
    lst=[]
    for i in string.split():
        lst.append(int(i))
    return lst

def compare(lst):
    lst1=deserialize(lst)
    if lst==lst1:
        print('Success!')

serialized=serialize(lst)        
file=input('Pls type in filename:')
file=pickle.dumps(serialized)
pickle.load(file)

compare(serialized)
         
         
