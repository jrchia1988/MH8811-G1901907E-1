
import pickle
import json

def serialize(lst):
    if type(lst)==list:
        string='list|'
        for i in lst:
            string+=str(i)
            string+='|'
            string+=str(type(i))
            string+='|'
        return string[:-1]
    elif type(lst)==dict:
        string='dict|'
        for i,v in lst.items():
            string+=str(i)
            string+='|'
            string+=str(type(i))
            string+='|'
            string+=str(v)
            string+='|'
            string+=str(type(v))
            string+='|'
        return string
    
def deserialize(string):
    a=string.split('|')
    if a[0]=='list':
        lst=[]
        for i in range(1,len(a)-1,2):
            if 'float' in a[i+1]:
                lst.append(float(a[i]))
            elif 'int' in a[i+1]:
                lst.append(int(a[i]))
            else:
                lst.append(a[i])
        return lst
    else:
        dct={}
        for i in range(1,len(a)-1,4):
            if 'float' in a[i+1]:
                b=float(a[i])
            elif 'int' in a[i+1]:
                b=int(a[i])
            else:
                b=a[i]
            if 'float' in a[i+3]:
                c=float(a[i+2])
            elif 'int' in a[i+3]:
                c=int(a[i+2])
            else:
                c=a[i+2]
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
with open(filename,'w') as a:
    pickle.dump(serialized,a)
a.close()
with open(filename,'r') as b:
    serial=pickle.load(b)
serial=deserialize(serial)
compare(data,serial)


         
