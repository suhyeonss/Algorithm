import sys
move = {'R': (1,0), 'L': (-1, 0), 'B': (0,-1), 'T':(0,1), 'RT': (1,1), 'LT':(-1, 1), 'RB':(1, -1), 'LB': (-1, -1)}
king, stone, N = sys.stdin.readline().split()
kLoc = [ord(king[0])-64, int(king[1])]
sLoc = [ord(stone[0])-64, int(stone[1])]
for _ in range(int(N)):
    movement = move[sys.stdin.readline().rstrip()]
    if kLoc[0] + movement[0] > 0 and kLoc[0] + movement[0] < 9 and kLoc[1] + movement[1] > 0 and kLoc[1] + movement[1] < 9:
        if sLoc==[kLoc[0] + movement[0], kLoc[1] + movement[1]]:
            if sLoc[0] + movement[0] > 0 and sLoc[0] + movement[0] < 9 and sLoc[1] + movement[1] > 0 and sLoc[1] + movement[1] < 9:
                kLoc = [kLoc[0] + movement[0], kLoc[1] + movement[1]]
                sLoc = [sLoc[0] + movement[0], sLoc[1] + movement[1]]
        else:
            kLoc = [kLoc[0] + movement[0], kLoc[1] + movement[1]]
print(chr(kLoc[0]+64)+str(kLoc[1]))
print(chr(sLoc[0]+64)+str(sLoc[1]))