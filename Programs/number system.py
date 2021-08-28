def ab(x):
    if(x==("F")):
        y=15
    elif(x=="E"):
        y=14
    elif(x=="D"):
        y=13
    elif(x=="C"):
        y=12
    elif(x=="B"):
        y=11
    elif(x=="A"):
        y=10
    elif(int(x)<10):
        y=int(x)
    return y

def ac(x):
    if(x==10):
        y="A"
    elif(x==11):
        y="B"
    elif(x==12):
        y="C"
    elif(x==13):
        y="D"
    elif(x==14):
        y="E"
    elif(x==15):
        y="F"
    elif(int(x)<10):
        y=str(x)
    return y


def ten_nother(begin,system):
    binar=""
    while(system>=begin):
        c=system%begin
        system=int(system/begin)
        binar=ac(c)+binar
    binar=ac(system)+binar
    return binar

def nother_ten(begin,system):
    i=len(system)
    sys=0
    for x in system:
        i-=1
        sys+=ab(x)*pow(begin,i)
    return sys


while(1==1):
    beginsystem= input("Введите начальную систему(от двоичной до шестнадцатиричной): ")
    finalsystem= input("Введите конечную систему (от двоичной до шестнадцатиричной): ")
    beginform=input("Введите значение (A,B,C,D,E писать по английски):")

    if(finalsystem=="10"):
       print(nother_ten(int(beginsystem),beginform))

    if(beginsystem=="10"):
        print(ten_nother(int(finalsystem),int(beginform)))

    if((finalsystem!="10") and (beginsystem!="10")):
        print(ten_nother(int(finalsystem),nother_ten(int(beginsystem),beginform)))
