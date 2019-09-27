import time

def hello_world():
    print('Hello World!')
    
def hello_user():
    name=input('What is your name?')
    print('Hello, ',name)
    
def convert_fahrenheit():
    temp=input('Pls enter temperature in Celsius:')
    print('The temperature in Faherenheit is ',(float(temp)*1.8+32))
    
def select_program():
    print('Do you want me to: \n1. greet the world?\n2. greet you?\n3. convert temperature from Celsius to Fahrenheit?')
    prog=input('Pls enter a number:')
    while prog!='q':
        if prog=='1':
            hello_world()
            time.sleep(2)
        elif prog=='2':
            hello_user()
            time.sleep(2)
        elif prog=='3':
            convert_fahrenheit()
            time.sleep(2)
        else:
            print('Error. Pls try again')
            time.sleep(2)
        print('Do you want me to: \n1. greet the world?\n2. greet you?\n3. convert temperature from Celsius to Fahrenheit?')
        prog=input('Pls enter a number (or press q to quit):')
        if prog=='q':
            print('We hope to see you again. Goodbye!')
        
 select_program()
  
