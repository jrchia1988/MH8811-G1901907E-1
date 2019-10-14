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
    for i in string.split('|'):
        lst.append(int(i))
    return lst

def compare(lst):
    lst1=deserialize(lst)
    if lst==lst1:
        print('Success!')

serialized=serialize(lst)        
file=input('Pls type in filename:')
filename=file+'.pkl'
a=open(filename,'wb')
pickle.dump(serialized,a)
a.close()
b=open(filename,'rb')
serialized=pickle.load(file,b)

compare(serialized)

#Homework

import json
filename=input('Pls select file: H1, H2, H3, H4, H5')
fh=open(filename)
data=json.load(fh)
fh.close()
serialized=serialize(data)
file=input('Pls type in filename:')
filename=file+'.pkl'
a=open(filename,'wb')
pickle.dump(serialized,a)
a.close()
b=open(filename,'rb')
serial=pickle.load(b)
if deserialize(serial)==data:
    print('Success!')


         
