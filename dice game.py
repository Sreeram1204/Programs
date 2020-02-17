import random
def call(n):
        if( n=='y' or n=='yes' or n=='YES'):
            print(random.randint(0, 5))
            data()
        if(n=='n'):
            print("end")
def data():
    n=input("enter y/n")
    call(n)

data()
