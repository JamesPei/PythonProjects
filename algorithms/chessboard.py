#__author__ = 'James'
#-*- coding:utf-8 -*-

def cover(board, lab=1, top=0, left=0, side=None):
    if side is None:side = len(board)

    #Side length of subboard:
    s = side //2

    #offsets for outer/inner squares of subboards:
    offsets = (0, -1),(side-1, 0)

    for dy_outer, dy_inner in offsets:
        for dx_outer, dx_inner in offsets:
            # if the  outer corner is not set...
            print '1:',top+dy_outer,left+dx_outer
            if not board[top+dy_outer][left+dx_outer]:
                #...label the inner corner:
                print '2:',top+s+dy_inner,left+s+dx_inner
                board[top+s+dy_inner][left+s+dx_inner] = lab

    # Next label:
    lab += 1
    print 's:',s
    if s>1:
        for dy in [0,s]:
            for dx in [0,s]:
                #recursive calls, if s is at least 2:
                for row in board:
                    print(("%3i"*8) % tuple(row))
                print '3:',lab, top+dy, left+dx, s
                lab = cover(board, lab, top+dy, left+dx, s)

    # return the next available label:
    return lab

board = [[0]*8 for i in range(8)]   #8*8 checkerboard
board[7][7] = -1    # missing corner
print cover(board)

for row in board:
    print(("%3i"*8) % tuple(row))
