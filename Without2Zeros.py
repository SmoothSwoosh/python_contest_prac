def No_2Zero(n, k):
    if n <= 0 or k <= 0:
        return 0
    if n == 1:
        return k - 1
    dp = [[0] * n for i in range(2)]
    dp[0][0] = 0
    dp[1][0] = k - 1
    for i in range(1, n):
        dp[0][i] = dp[1][i - 1]
        dp[1][i] += (dp[0][i - 1] + dp[1][i - 1]) * (k - 1)
    return dp[0][-1] + dp[1][-1]
