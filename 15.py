size = 20
memo = [[0 for x in range(size+2)] for y in range(size+2)]
memo[size][size] = 1
for x in range(size,-1,-1):
    for y in range(size,-1,-1):
        memo[x][y] += memo[x+1][y] + memo[x][y+1]
    y=size

print(memo[0][0])
