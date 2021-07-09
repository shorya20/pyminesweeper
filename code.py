#Shorya Sinha 101165008 
import random#random module
def main():
    global board
    board=[]#board will store the values of the created board
    trap_map=[]#trap map will store the values of the traps of the map
    global randnum
    randnum=random.randint(5,10)#randum size of the game is generated
    def create_board():
        x=random.randint(1,randnum)#random number from 1 to randnum
        board=[['-']*randnum for t in range(randnum)]#2d list created
        board[0][x-1]='G'#G added to a random spot in the first 
        for t in range(randnum):
            board[1][t]='P'
        rcount=0#count the amount of times R appears in the last row
        bcount=0#count the amount of times B appears in the last row
        while True:
            bishoprand=random.randint(1,randnum)
            rookrand=random.randint(1,randnum)
            if int(bishoprand) != int(rookrand):
                if board[randnum-1][rookrand-1]!='B' and board[randnum-1][rookrand-1]!='R':
                    if bcount!=2:
                        board[randnum-1][rookrand-1]='B'
                        bcount+=1
            if int(bishoprand) != int(rookrand):
                if rcount!=2:
                    if board[randnum-1][bishoprand-1]!='R' and board[randnum-1][bishoprand-1]!='B':
                        board[randnum-1][bishoprand-1]='R'
                        rcount+=1
            if rcount==2 and bcount==2:
                break
        return board
    def set_traps():
        trap_map=[[' ']*randnum for t in range(randnum)]#trap map is initialised
        for t in range(2,randnum-1):#from 2nd row to 2nd last row
            for x in range(randnum):
                trapnum=random.randint(1,randnum)#probability calculated with being a chance of 2 out of 10
                if trapnum<=2:
                    trap_map[t][x]='T'
        return trap_map
    def display_board():
        count=0
        r=list(range(randnum))
        t=''#will store the randnum as 0123... for the top line
        l=''#will store = depending on the randnum
        b=''#will store the randnum as 0123... for the bottom line
        a=''#will store = depending on the randnum
        for x in range(len(r)):
            i=r[x]
            t+=str(i)
        print('    ',t)#prints t in order
        for k in range(len(r)):
            y='='
            l+=y
        print('   ','+'+l+'+')#arranges l and prints l
        for x in range(len(p)):
            g=p[x]#takes an element x from the board p
            print(str(count)+'|'+' '.join(g)+'|'+str(count))#joins the element between 2 '|' 
            count=count+1
        for q in range(len(r)):
            s=r[q]
            b+=str(s)
        print('    ',b)#prints b in order
        for i in range(len(r)):
            w='='
            a+=w
        print('   ','+'+a+'+')#arranges a and prints +
    def validate_moves(currentrow,currentcol,newposrow,newposcol):
        piece=p[int(currentrow)][int(currentcol)]#currentpiece in question
        newpos=p[int(newposrow)][int(newposcol)]#newposition of the piece to be placed
        if int(newposrow)==0:#if the newpositionrow is 0
            pcount=0
            for y in range(randnum):
                if p[1][y]=='P':#if the newposition contains 'P' then score+1
                    pcount+=1
            if pcount<len(p):
                return True
            elif pcount==len(p):
                return False
        if piece=='R':#if current piece is rook
            if newpos!='R' and newpos!='B': #if newposition does not contain rook or bishop
                if int(newposrow)==int(currentrow):#if same row
                    return True#valid move
                if int(newposcol)==int(currentcol):#if same column
                    return True#valid move
                else:
                    return False
            else:
                return False
        elif piece=='B':#if current piece is rook
            if newpos!='R' and newpos!='B': #if newposition is not rook or bishop
                diff1=int(newposcol)-int(currentcol)#since bishop moves in a symmetrical fashion
                diff2=int(currentrow)-int(newposrow)
                diff3=int(currentcol)-int(newposcol)
                diff4=int(newposrow)-int(currentrow)
                if diff1==diff2:
                    return True
                if diff3==diff4:
                    return True
                if diff2==diff3:
                    return True
                if diff1==diff4:
                    return True
                else:
                    return False
            else:
                return False
        elif piece=='G':
            for y in range(randnum):
                if p[0][y]=='G':#if G is there in the first row
                    return True
        else:
            return False
    def check_traps(currentrow,currentcol,newposrow,newposcol,trap):
        #base case
        if currentrow==newposrow and currentcol==newposcol:#if the newcol=currentcol and currentrow=newposrow after recursion tries
            return False
        #recursive case
        if trap[currentrow][currentcol]=='T':#if the current row and column in the pathway of the repsected piece contains a trap
            p[currentrow][currentcol]='T'#p is updated with T in place of the trap
            return '{} : {},{}'.format("Trap at",currentrow,currentcol)
        else:
            if currentrow>newposrow and newposcol>currentcol:#for bishop
                return check_traps(int(currentrow)-1,int(currentcol)+1,int(newposrow),int(newposcol),trap)
            elif currentrow>newposrow and currentcol>newposcol:#for bishop 
                return check_traps(int(currentrow)-1,int(currentcol)-1,int(newposrow),int(newposcol),trap)
            elif currentrow==newposrow and currentcol>newposcol:#rook
                return check_traps(int(currentrow),int(currentcol)-1,int(newposrow),int(newposcol),trap)
            elif currentrow==newposrow and currentcol<newposcol:#rook
                return check_traps(int(currentrow),int(currentcol)+1,int(newposrow),int(newposcol),trap)
            elif currentrow>newposrow and currentcol==newposcol:#rook
                return check_traps(int(currentrow)-1,int(currentcol),int(newposrow),int(newposcol),trap)
    def move_general(p):
        x=random.randint(1,randnum)#random position for general to be placed in
        generalpos=0
        for y in range(randnum):
            if p[0][y]=='G':#place general in random place
                generalpos=int(y)
        p[0][generalpos]='-'#current position is switched with '-'
        p[0][int(x)-1]='G'
        return p
    def move_soldier(currentrow,currentcol,newposrow,newposcol):
        global score
        currentpiece=p[int(currentrow)][int(currentcol)]#currentpiece in position
        newpiece=p[int(newposrow)][int(newposcol)]#newpiece in position
        if newpiece=='P':#if newpiece is a pawn
            score+=2#score is updated
            p[int(currentrow)][int(currentcol)]='-'#currentpiece is removed
            p[int(newposrow)][int(newposcol)]=str(currentpiece)#currentpiece takes place of pawn
            return p
        if newpiece=='G':#if newpiece is general
            p[int(currentrow)][int(currentcol)]='-'#currentpiece is removed
            p[int(newposrow)][int(newposcol)]=str(currentpiece)#currentpiece takes place of general
            score+=10#score is added
        if newpiece=="-":#if the newpiece is no piece
            p[int(currentrow)][int(currentcol)]='-'#currentpiece is removed
            p[int(newposrow)][int(newposcol)]=str(currentpiece)#newpiece is updated
            return p
        else:
            return p
    def game_over(p):
        check1= any('B' in h for h in p)#check1 if any 'B' in h for h element in p
        check2= any('R' in g for g in p)#check2 if any 'R' in g for g element in p
        if check1==True or check2==True:
            return False#returns false that there is r and g
        if check1==False and check2==False:
            return True#returns true if no g or r
    global score
    score=0
    print("Welcome to this Minesweeper-style chess game where you as the player have 2 rooks and bishops to move")
    print()
    print()
    print("The game consists of a general to defeat. The general only moves across the row it's placed in. ")
    print()
    print("The player cannot advance until they've moved and defeated the pawns which are stationary and are to defend the general")
    print()
    print("The difficulty lies wherein there will be traps placed your way towards the position you send your bishops and rooks")
    print("If the soldier comes across a trap in it's way, it's unfortunately dead")
    print()
    print("and remember the traps fluctuate and change their positions based on every move you make!")
    print()
    print("B can move diagonally in four different directions, i.e., left-up, right-up, left-down and right-down.")
    print()
    print("R can move in a straight line in four different directions, i.e., left, right, up, and down.")
    print()
    print("G, B, R cannot move to a location if that location is already occupied by another soldier.")
    print()
    print("Game Starts Now!! >> ")
    global trap
    trap=set_traps()
    global p
    p=create_board()#p is the board which will be used as the global board to update all the values
    display_board()
    while True:
        try:
            global currentrow
            global currentcol
            currentrow,currentcol=input("To move your soldier enter its current position <row,col> ").split(',')#saves the values of with ',' to differentiate them
            global newposrow
            global newposcol
            newposrow,newposcol=input("Enter the new position <row,col>").split(',')#^
        except:
            print('Error occured')
            break
        if int(newposrow)>=int(randnum):
            print("Sorry range is out of bounds")
            break
        if int(newposcol)>=int(randnum):
            print("Sorry range is out of bounds")
            break
        if int(currentrow)>=int(randnum):
            print("Sorry range is out of bounds")
            break
        if int(currentcol)>=int(randnum):
            print("Sorry range is out of bounds")
            break
        valid=validate_moves(currentrow,currentcol,newposrow,newposcol)
        currentrow=int(currentrow)
        currentcol=int(currentcol)
        newposrow=int(newposrow)
        newposcol=int(newposcol)
        global soldier
        soldier=p[currentrow][currentcol]
        if valid==True:
            check=check_traps(currentrow,currentcol,newposrow,newposcol,trap)
            if check!=False:
                p[currentrow][currentcol]='-'
                p=move_general(p)
                print(check)
                score-=2
            else:
                p=move_soldier(currentrow,currentcol,newposrow,newposcol)
                if score<=10:
                    p=move_general(p)
        if valid==False:
            print("Invalid move")
        if score>=10:
            print("You win")
            print("Your score:",score)
            display_board()
            break
        gameover=game_over(p)
        if gameover==True:
            print("Game Over.\nAll your soldiers are dead")
            print("Your score:",score)
            break
        print("Your score:",score)
        display_board()
main()                 
