def main():
    m, n = map(int, input().split())
    H = list(map(int, input().split()))
    D = list(map(int, input().split()))
    
    dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
    dp[0][0] = 0 
    
    for i in range(1, m+1):
        for j in range(n+1):
            if dp[i-1][j] != -1:
                dp[i][j] = max(dp[i][j], dp[i-1][j])
                new_hm = min(j + H[i-1], n)
                if new_hm <= n:
                    dp[i][new_hm] = max(dp[i][new_hm], dp[i-1][j])
                
                if j == n:
                    dp[i][j] = max(dp[i][j], dp[i-1][j] + D[i-1])
    
    max_dollars = max([dp[m][j] for j in range(n+1)])
    print(max_dollars)

if __name__ == '__main__':
    main()
