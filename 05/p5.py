#C1

import pickle

def serialize(lst):
    string=''
    for i in lst:
        string+=i
    file=input('Pls type in filename:')
    file=pickle.dumps(string)
    print(pickle.load(file)) 
    
def deserialize(string):
    lst=[]
    for i in string.split():
        lst.append(i)
    return lst

def compare(lst1,lst2):
    if lst1==lst2:
        print('Success!')
        
    
         
         
