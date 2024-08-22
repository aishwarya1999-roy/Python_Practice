def solve():
    return

m = [[1,0,0,0],
     [1,1,0,1],
     [1,1,0,0],
     [0,1,1,1]]
n = len(m)
ans = ''
srcX = srcY = 0
visited = [[0 for _ in range(n)] for _ in range(4)]
path = ''
solve(m,n,ans,srcX,srcY,visited,path)
ans.sort()
print(ans)




