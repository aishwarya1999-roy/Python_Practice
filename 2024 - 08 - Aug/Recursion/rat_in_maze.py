# def solve():
#     return

m = [[1,0,0,0],
     [1,1,0,1],
     [1,1,0,0],
     [0,1,1,1]]
n = len(m)
# ans = ''
# srcX = srcY = 0
visited = [[0 for _ in range(4)] for _ in range(4)]

for i in range(4):
    for j in range(4):
        visited[i][j] = 0

print(visited)




