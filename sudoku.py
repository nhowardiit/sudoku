import numpy as np
import os, sys, time, copy


def newPuzzle():
    puz = [[0,0,0,2,6,0,7,0,1],
        [6,8,0,0,7,0,0,9,0],
        [1,9,0,0,0,4,5,0,0],
        [8,2,0,1,0,0,0,4,0],
        [0,0,4,6,0,2,9,0,0],
        [0,5,0,0,0,3,0,2,8],
        [0,0,9,3,0,0,0,7,4],
        [0,4,0,0,5,0,0,3,6],
        [7,0,3,0,1,8,0,0,0]]
    return puz 

def printPuzzle(puz):
    os.system('clear')
    print("""     _1___2___3___4___5___6___7___8___9_
    """)
    for i in range(9):
        print(i + 1, '  [ ', end='')
        for j in range(9):
            print(puz[i][j],'| ',end='')
        print()

def manual(puz):
    while True:
        printPuzzle(puz)
        puz = nextMove(puz)
        isSolved(puz)

def getCheckInput(request):
    while True:
        x = input(request)
        if x.lower() == "exit" or x.lower() == "e":
            os.system('clear')
            sys.exit("Good Bye")
        try:
            x = int(x)
        except ValueError:
            print("Please enter a value between 1 and 9")
            continue
        if x < 1 or x > 9:
            print("Please enter a value between 1 and 9")
            continue
        else:
            return x

def nextMove(puz):
    #the minus ones translate input for zero indexed arrays
    col = getCheckInput('Column : ') - 1
    row = getCheckInput('Row    : ') - 1
    val = getCheckInput('Value  : ')
    try:
        if checkCell(puz, row, col, val):
            puz[row][col] = val
    except ValueError as error:
        print(error)
        time.sleep(3)
    return puz

def solver(pPuz,pRow,pCol):
    cPuz = copy.deepcopy(pPuz)
    printPuzzle(cPuz)

    #this will check if we are at the end of row and jump to the next row
    if pCol < 8:
        nxtCol = pCol+ 1
        nxtRow = pRow
    else:
        nxtCol = 0
        nxtRow = pRow + 1

    #check if current cell is empty
    if cPuz[pRow][pCol] == 0:
        validVal = [1,2,3,4,5,6,7,8,9]

        while True:
            #check to see if there are any more valid options in this square
            if len(validVal) == 0:
                #check to see if we are at the star
                if pRow == 0 and pCol == 0:
                    sys.exit("Unable to solve")
                else:
                    #go back up on level in recursion and try again
                    return
        
            #try next valid value and check puzzle
            val = validVal.pop()
            print(pRow, pCol, val)
            time.sleep(.05)
            try:
                #checks if val is valid in cell
                if checkCell(cPuz, pRow, pCol, val):
                    #update cell with valid value
                    cPuz[pRow][pCol] = val
                    #check if the puzzle is solved
                    isSolved(cPuz)
                    #keep going
                    solver(cPuz, nxtRow, nxtCol)
                    #This resets the cell so more guesses can happen
                    cPuz[pRow][pCol] = 0
            except:
                continue
    
    #current cell is not empty so move to next cell
    else:
        solver(cPuz,nxtRow,nxtCol)



def checkCell(puz, row, col, val):
    #Check if desired cell is empty
    if puz[row][col] != 0:
        raise ValueError("That cell is not empty")

    #Check Column
    for i in range(9):
        if val == puz[i][col]:
            raise ValueError("That value is present in column")
    
    #Check Row
    for i in range(9):
        if val == puz[row][i]:
            raise ValueError("That value is present in row")
    
    #Check Block
    for i in range(3):
        for j in range (3):
            if val == puz[(int(row/3)*3)+i][(int(col/3)*3)+j]:
                raise ValueError("That value is present in block")
    
    #If checks pass return true
    return True

def isSolved(puz):
    for i in range(9):
        for j in range(9):
            #if there are still zeros in the puzzle its not solved
            if puz[i][j] == 0:
                return False
            #if there are no zeros and all tests pass the game is over
            elif i==8 and j==8:
                #Puzzle is solved
                #maybe not best practice to exit here
                #probably should return true but i am done with this program
                printPuzzle(puz)
                print("Good Job!")
                time.sleep(5)
                main()

def main():
    os.system('clear')
    puz = newPuzzle()
    while True:
        print("( 1 ) - (S)olver")
        print("( 2 ) - (M)anual")
        print("( 3 ) - (E)xit")
        gt = input("""Which game type would you like?
        # """)
        if gt == '1' or gt.lower() == "solver" or gt.lower() == "s":
            solver(puz,0,0)
        elif gt == '2' or gt.lower() == "manual" or gt.lower() == "m":
            manual(puz)
        elif gt == '3' or gt.lower() == "exit" or gt.lower() == "e":
            os.system('clear')
            sys.exit("Good Bye")
        else:
            print("Please choose valid game type")


if __name__ == '__main__': main()