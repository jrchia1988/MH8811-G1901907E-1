
import pickle
import json

def serialize(lst):
    string=str(type(lst).__name__)
    if (type(lst)==list)|(type(lst)==tuple)|(type(lst)==set):
        for i in lst:
            string+=str(i)
            string+='|'
            string+=str(type(i).__name__)
            string+='|'
    else:
        for i,v in lst.items():
            string+=str(i)
            string+='|'
            string+=str(type(i).__name__)
            string+='|'
            string+=str(v)
            string+='|'
            string+=str(type(v).__name__)
            string+='|'
    return string[:-1]
    
def deserialize(string):
    a=string.split('|')
    if (a[0]=='list')|(a[0]=='set')|(a[0]=='tuple'):
        lst=[]
        for i in range(1,len(a)-1,2):
            b=eval(a[i+1]+'('+a[i]+')')
            lst.append(b)
        if (a[0]=='set')|(a[0]=='tuple'):
            lst=eval(a[0]+'('+lst+')')
        return lst
    else:
        dct={}
        for i in range(1,len(a)-1,4):
            b=eval(a[i+1]+'('+a[i]+')')
            c=eval(a[i+3]+'('+a[i+2]+')')
            dct[b]=c
        return dct
        
def compare(lst1,lst2):
    if type(lst1)==type(lst2):
        if lst1==lst2:
            print('Success!')
        else:
            print('Fail')
    else:
        print('Fail')

file=input('Pls select file: H1-1,H1-2,H1-3,H1-4,H1-5.')
filename=file+'.json'
with open(filename,'r') as fh:
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
serial=deserialize(serial)
compare(data,serial)


         
