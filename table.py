import time
from datetime import datetime

def digitMenu():
    opList=[]
    size=input("Enter the starting number for table:")
    print("We will start from table of " + size + " and go till 20.")
    return int(size)
    
def posNumGen(opList):
    size=opList[0]
    augList=[]
    i=0
    for i in range(int(num)):
        aug=random.randint(0,maxNum(size))
        augList.append(aug)
        i=i+1
    #faug = random.randint(0,maxNum(num))
    #saug = random.randint(0,maxNum(num))
    return augList
    
def check(ques,ans,uans):
    #uans=input('Enter your answer here: ')
    if(uans!='x'):
        while str(ans)!=str(uans) :
            uans=input("Oops, wanna try again??")
            if(uans=='x'):
                return uans
        #print(uans)
        #print(ans)
        print("Great job")
    else:
        return uans
    
def table():
    close ='y'
    options=digitMenu()
    while options < 21:
        print("You are starting table of " + str(options))
        #start_time = time.clock()
        start_time = datetime.now()
        for i in (1,2,3,4,5,6,7,8,9,10):
            uans=input(str(options) + " X " + str(i) + " : " )
            ques=str(options) + " X " + str(i) + " : " 
            ans = options * i
            check(ques,ans,uans)
      
        #print( time.clock() - start_time + " seconds")
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        options = options + 1

        
table()
        

