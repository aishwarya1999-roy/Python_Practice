def min_cost_to_transform(A, B, insert_cost, delete_cost, substitute_cost):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i * delete_cost
    
    for j in range(n + 1):
        dp[0][j] = j * insert_cost
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i-1] == B[j-1]:
                cost = dp[i-1][j-1]  # No cost if characters are the same
            else:
                cost = dp[i-1][j-1] + substitute_cost  # Substitution cost
            
            dp[i][j] = min(
                cost,                # Substitution
                dp[i-1][j] + delete_cost,  # Deletion
                dp[i][j-1] + insert_cost   # Insertion
            )
    
    return dp[m][n]

A = 'abcdef'
B = "aefdcd"
