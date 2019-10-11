#C1

import pickle

def serialize():
    user_list=[]
    while ans!='q':
         ans=input('Please key in an integer:')
         try:
            val=int(ans)
         except:
            ans='q'
            print('Pls try again.')
         user_list.append(val)
    serial=input('Pls type in filename.')
    serial=pickle.dumps(user_list)
    return serial
         
         
