while(1==1):
    feb=[0,1]
    void=input("Введите номер числа фибоначи: ")
    while(len(feb)<int(void)):
        feb.append(feb[-1]+feb[-2])
    if(int(void)!=1):
        print(feb)
    else:
        print(feb[0])
