from datetime import date, timedelta
from os import read
import getpass
import os



clear = lambda: os.system('cls')
 


aaj = date.today()
today = aaj.strftime("%d/%m/%Y")

kal = aaj - timedelta(days = 1)
yesterday = kal.strftime("%d/%m/%Y")




def isToday():
    with open("H:\\log.txt") as f:
        content = f.read()
        
        if today in content :
            return 1
        else : 
            return 0    

def writeDone(taarik , task):


    finalContent = ""
    while True:
        f = open("H:\\log.txt")
        content = f.read()
        index = content.index(taarik) + 11
        write1 = content.find(task , index , len(content) - 1) + 2
        f.close()

        finalContent = list(content)
        finalContent.insert(write1 , " (Done) ")

        finalContent = ''.join(finalContent)

        more = input(" any more done task ? (y/n) " )
      
        if(more == 'y'):
            task = input("Task no. ?  ")
            task = task + "."
            continue
        else:
            break

    # print(str(finalContent))

    f = open("H:\\log.txt" , "w")
    
    f.write(str(finalContent))
    f.close

    
        

        

    


def doneList():
    taarik = input("Enter the date of done list in DD/MM/YYYY/nor press t for today\ny for yesterday\n")

    if taarik == 't':
        taarik = today
    elif taarik == 'y':
        taarik = yesterday
    
    if readMode(taarik):
        readMode(taarik)
        task = input("Enter the completed task : ")
        writeDone(taarik , task)
    else:
        print("Date doesn't exists:\n")
        return




def readMode( taarik = today ):
   
    clear()  
    with open("H:\\log.txt") as f:
        content = f.read();
    if taarik == today:

        if yesterday in content :
            index = content.index(yesterday)
            print(content[index:])

        elif today in content :

            index = content.index(today)
            print(content[index:])

        else:
            print("Nothing To Display Here")

    elif taarik in content :

        index = content.index(taarik)
        index2 = 10
        length = len(content)
        for i in range(index + 10,length):
            if content[i] == '/':
                index2 = i-3 
                break
            if i == length-1:
                print(content[index:])
                return 1

        print(content[index:index2:1])
        return 1
    else:
        return 0 

    return 1
   
      

def writeMode():
    clear()  
    with open("H:\\log.txt" ,"a") as f:
        print("\n\nWrite Mode")
        for i in range(100):
            print('_', end="")
            f.write("_")
        f.write(f"\n\n{today} :-\n");

        i = 1
        fill = ""

        print("\n")
        while True:
            fill = input(f"\nEnter in {i}.  : ")
            f.write(f"{i}. {fill}\n")
            i += 1
            choose = input("Enter More ? : ")
            if choose == 'y' or choose == 'Y' :
                continue
            break
    clear()        




while True:

    for i in range(100):
        print('_', end="")
    choice = input("\n1. READ MODE\n2. WRITE MODE\n3. Enter in DONE list\nPRESS ANY OTHER KEY TO EXIT\n")

    

    if choice == '1':
        # read mode 
        readMode()

    elif choice == '2':
        clear()
        if isToday():
            todo = input("\nTodays Log Already Exists\n\nWant to make DONE list? (y/n) : ")

            if(todo == 'y' or todo == 'Y'):
                doneList()
        else :
              
            try:
                p = getpass.getpass()
            except Exception as error:
                print('ERROR', error)


            if p == "qwertyrbR1@" :
                writeMode()
            else:
                print("Try Again !")

    elif choice == '3':
        doneList()
    else:
        exit()
