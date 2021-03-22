import random

def maxNum(num):
    i=0
    maxNum=''
    while(i < int(num)):
        #print(i)
        maxNum=maxNum+"9"
        i=i+1
        #print(maxNum)
    return int(maxNum) 


def digitMenu():
    opList=[]
    close='y'
    while close !='z':
        size=input("Enter max number of digits you want to be used:")
        try:
            int(size)
            close='z'
        except ValueError:
            close='y'
    opList.append(size)
    while close !='x':
        num =input("Enter number of numbers you want to be used:")
        try:
            int(num)
            close='x'
        except ValueError:
            close='y'
    opList.append(num)
    return opList
    
def posNumGen(opList):
    size=opList[0]
    num=opList[1]
    #print('size')
    #print(size)
    #print(num)
    augList=[]
    i=0
    for i in range(int(num)):
        aug=random.randint(0,maxNum(size))
        augList.append(aug)
        i=i+1
    #faug = random.randint(0,maxNum(num))
    #saug = random.randint(0,maxNum(num))
    return augList
    
def check(ans):
    close = 'y'
    while close !='z':
        uans=input('Enter your answer here: ')
        try:
            int(uans)
            close='z'
        except ValueError:
            close='y'
    if(uans!='x'):
        while int(ans)!=int(uans):
            uans=input("Oops, wanna try again??")
            if(uans=='x'):
                return uans
        #print(uans)
        #print(ans)
        print("Great job")
    else:
        return uans
        
def addition():
    close ='y'
    options = digitMenu()
    while close:
        augList=posNumGen(options)
        argCount = len(augList)
        oprCount = 1
        if argCount > 0 :
            sumOfNums = 0
            listOfNum = ''
#        print(args[0])
            for elem in augList :
                #print(elem)
                if(oprCount==1):
                    listOfNum=str(elem) 
          #  elif(oprCount== argCount):
          #      listOfNum=listOfNum + str(elem) 
                elif(oprCount==argCount):
                    listOfNum=listOfNum + " + " + str(elem) + " = ? "
                else:
                    listOfNum=listOfNum + " + " + str(elem)
                oprCount = oprCount + 1
            #print('kuch bhi')

                sumOfNums =  int(sumOfNums) + int(elem)
            print(listOfNum)
                #print(sumOfNums)
#            uans=input('Enter your answer here: ')
#            if(uans!='x'):
            #print('oprCount')
            #print(oprCount)
            #print('argCount')
            #print(argCount)
            if(check(sumOfNums)=='x'):
                return quit()#'x'
addition()