def minCost(cost):
    n = len(cost)
    dp = [float('inf')] * (1 << n)
    dp[0] = 0

    for mask in range(1 << n):
        task = bin(mask).count("1")

        for worker in range(n):
            if not (mask & (1 << worker)):
                newMask = mask | (1 << worker)
                dp[newMask] = min(dp[newMask],
                                  dp[mask] + cost[worker][task])

    return dp[(1 << n) - 1]


# -------- TEST --------
if __name__ == "__main__":
    cost = [
        [9,2,7],
        [6,4,3],
        [5,8,1]
    ]

    print(minCost(cost))
