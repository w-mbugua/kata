n = int(input())
def jumpingOnClouds(c):
    position = jumps = 0
    
    while position < n -1:
        if position < n - 2 and c[position + 2] == 0:
            position += 2
        else:
            position += 1
        jumps += 1
    return jumps

# Hackerrank challenge. c is an array of n binary integers. The zeros are the safe clouds. The function return the least number of jumps possible