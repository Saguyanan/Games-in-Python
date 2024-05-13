Row1 = ['|1|', '|2|', '|3|']
Row2 = ['|4|', '|5|', '|6|']
Row3 = ['|7|', '|8|', '|9|']
TTT = (Row1, Row2, Row3)
x = False
XorY = ''
Count = 0
Numlist = []
Win = False
def WinCon():
    for x in Numlist:
        if x + 3 and x + 6 in Numlist:
            print(f'{XorY} Wins!')
            Win = True
        if x + 1 and x + 2 in Numlist:
            print(f'{XorY} Wins!')
            Win = True
        if x + 4 and x + 8 in Numlist:
            print(f'{XorY} Wins!')
            Win = True
        if x + 3 and x + 4 in Numlist:
            print(f'{XorY} Wins!')
            Win = True
        if Win == True:
            Choice = input('Play again?')
            
def Boardprint():
    print(Row1)
    print(Row2)
    print(Row3)

def Turn():
    global Count
    Count += 1
    if Count > 9:
        print("Cat's game")
    if Count % 2 == 0:
        X = True
        print("Its X's turn")
    elif Count % 2 != 0:
        X = False
        print("Its O's turn")
    if X == True:
        XorY = '|X|'
    if X == False:
        XorY = '|O|'    
    Move = input('in Which postion will you play?')
    Numlist.append(int(Move))
    for T in TTT:
        print(T)
        for Y, X in enumerate(T):
            if X[1] == Move:
                if int(X[1]) <= 3: 
                    Row1[Y] = XorY
                elif int(X[1]) > 3 and int(X[1]) <= 6:
                    Row2[Y] = XorY
                elif int(X[1]) > 6 and int(X[1]) <= 9:
                    Row3[Y] = XorY
            print(X)
        Boardprint()
        WinCon()            
    Turn()


Turn()
print(TTT)