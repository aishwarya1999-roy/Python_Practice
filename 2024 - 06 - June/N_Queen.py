class Solution:
    def solveNQueens(self, n: int):
        col = set()
        posdiag = set()
        negdiag = set()
        count = 0
        result = []

        board = [["."]*n for i in range(n)]

        def backtrack(r):
            nonlocal count
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return 

            for c in range(n):
                if c in col or r+c in posdiag or r-c in negdiag:
                    continue
                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c] = "Q"
                backtrack(r+1)

                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c] = "."
                count=count+1
        count = 0 
        backtrack(0)
        return count
    
if __name__ == "__main__":
    solution = Solution()
    result = solution.solveNQueens(4)
    print(result)
