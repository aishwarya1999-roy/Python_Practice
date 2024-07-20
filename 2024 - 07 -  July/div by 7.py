def minimum_buying_days(N, S, M):
    if N < M:
            return -1
        if (N-M)*6 < M and S > 6:
            return -1
        if (S*M)%N == 0 and N == M and S > 6:
            ans = -1
        elif (S*M)%N == 0:
            ans = (S*M)//N
        else:
            ans = (S*M)//N + 1
        return ans

print(minimum_buying_days(9, 10, 8))
print(minimum_buying_days(2, 5, 2))
print(minimum_buying_days(24, 35, 20))
