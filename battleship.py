import random


def hitchecker(x, y, grid):
    '''Parameters are x,y inputs into the board ' X' at given cordinate'''

    if grid[y][x] == ' X':
        print 'Player: ' + name, "               ", 'Score: ', points
        print ""
        counter = 0
        for rows in grid:
            print counter, rows
            print ""
            counter += 1
        for items in range(len(grid[1])):
            print '   ', items,
        print ""
        print""
        print 'Already attacked here,try somewhere else.'

    else:

        if x >= 0 and y >= 0:
            print 'Player: ' + name, "               ", 'Score: ', points
            print ""
            try:
                grid[y][x] = ' X'
            except Exception:
                print 'Please choose a cordinate within the plane'
                counter = 0
            for rows in grid:
                print counter, rows
                print ""
                counter += 1
            for items in range(len(grid[1])):
                print '   ', items,
            print ""
            print""
            print 'Miss! Try Again'


def hit(x, y, grid):
    '''Checks for x and y for the computer's ship and marks that spot 'O'''
    if x >= 0 and y >= 0:
        print 'Player: ' + name, "               ", 'Score: ', points
        print ""
        grid[y][x] = ' O'
        counter = 0
        for rows in grid:
            print counter, rows
            print ""
            counter += 1
        for items in range(len(grid[1])):
            print '   ', items,


def computer(x, y, grid):
    ''' The computer makes a random guess on the grid and places an 'X'''
    if x == ranx and y == rany:
        print 'Player: ' + name, "               ", 'Score: ', points
        print ""
        grid[y - 1][x - 1] = ' X'
        counter = 0
        for row in grid:
            print counter, row
            print ""
            counter += 1
        for items in range(len(grid[1])):
            print '   ', items,
    elif grid[y][x] == ' #':
        print 'Player: ' + name, "               ", 'Score: ', points
        print ""
        grid[y][x] = ' *'
        counter = 0
        for rows in grid:
            print counter, rows
            print ""
            counter += 1
        for item in range(len(grid[1])):
            print '   ', item,
            print""
            print"Sink!"

    else:
        print 'Player: ' + name, "               ", 'Score: ', points
        print ""
        grid[y][x] = ' X'
        counter = 0
        for row in grid:
            print counter, row
            print ""
            counter += 1
        for item in range(len(grid[1])):
            print '   ', item,


def shipmaker(x, ranx, rany):
    ''' Makes the ship and and places them on the grid'''
    counter = 0
    op = [1, 2]
    chooser = random.choice(op)

    if chooser == 1:
        for k in range(x):
            grid[rany][ranx - counter] = ' #'
            counter += 1

    else:
        for item in range(x):
            grid[rany - counter][ranx] = ' #'
            counter += 1

bdsize = 0
shpsize = 0
numshp = 0
name = raw_input(" Enter your name: ")
while (True):
    try:
        print ""
        boardsize = raw_input(" Please enter the board size: ")
        bdsize = int(boardsize)
        break
    except Exception:
        print''
        print 'Please input a valid board size'

while(True):
    try:
        print""
        shipinput = raw_input(" Please enter the ship size (2,3,4,5): ")
        shpsize = int(shipinput)
        if shpsize > 5 or shpsize < 2:
            print""
            print 'Please put a valid ship size'
        else:
            break
    except Exception:
        print''
        print 'Please input a valid ship size'

grid = [['  ' for item in range(bdsize)]for items in range(bdsize)]

ranlst = []
for items in range(bdsize):
    ranlst.append(items)
ranx = random.choice(ranlst)
rany = random.choice(ranlst)
ranshx = random.choice(ranlst)
ranshy = random.choice(ranlst)
shipmaker(shpsize, ranshx, ranshy)
points = 0
counter = 0
checker = 0
cory = 0
corx = 0
print""
print""
print 'Legend :'
print""
print 'Ship', '#'
print""
print  'Hit Ship', ' O'
print""
print 'Hit', ' X'
print ""
print ""

print 'Player: ' + name, "               ", 'Score: ', points
print ""

for rows in grid:
    print counter, rows
    print ""
    counter += 1
for items in range(len(grid[1])):
    print '   ', items,

print " ",


while (True):
    if checker == 0:
        try:
            print ""
            guessx = raw_input(" Please enter the x cordinate: ")
            guessy = raw_input(" Please enter the y cordinate: ")
            corx = int(guessy)
            cory = int(guessx)
            if corx < 0 and cory < 0:
                print""
                print 'Please enter a value(s) greater than 0'
            else:
                grid[cory][corx]
                checker += 1
        except Exception:
            print ""
            print 'Invalid input, please enter again'
            cheker = 0
    elif cory == ranx and corx == rany:
        computer(cory - 1, corx - 1, grid)
        print""
        points += 1
        hit(cory, corx, grid)
        print ''
        print""
        print 'You hit a ship'
        checker = 0
    elif cory == ranx - 1 and corx == rany:
        computer(cory - 1, corx - 1, grid)
        print""
        points += 1
        hit(cory, corx, grid)
        print ''
        print 'You hit a ship'
        checker = 0
    else:
        hitchecker(cory, corx, grid)
        print ""
        computer(cory - 1, corx - 1, grid)
        checker = 0
