def solve(m,n,ans,x,y,visited,path):
    if x == n-1 and y == n-1:
        ans.append(''.join(path[:]))
    return


def rat(m,n):
    ans = []
    srcX = srcY = 0
    if m[0][0]==0:
        return ans
    visited = [[0 for _ in range(n)] for _ in range(4)]
    path = []
    solve(m,n,ans,srcX,srcY,visited,path)
    ans.sort()
    return ans

m = [[1,0,0,0],
     [1,1,0,1],
     [1,1,0,0],
     [0,1,1,1]]
n = len(m)

print(rat(m,n))


