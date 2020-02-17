def data():
    print("what is your choice:")
    print("1.go to college")
    print("2.go on vacation")
    print("3.take rest")
    print("4.play game")
    print("q.quit")
    e=input()
    if(e=='1' or e=='2' or e=='3' or e=='4'):
        data()
    elif(e=='q'):
        print("the end")
data()
        
