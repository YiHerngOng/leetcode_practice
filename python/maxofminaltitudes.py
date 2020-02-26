class Solution:
    def sol(self, nums):
        
        N = len(nums)
        M = len(nums[0])

        nums[0][0] = 1e9
        nums[N - 1][M - 1] = 1e9

        dp = [[1e9] * M for i in range(N)]

        for j in range(1, M):
            dp[0][j] = min(dp[0][j - 1], nums[0][j])
        for i in range(1, N):
            dp[i][0] = min(dp[i - 1][0], nums[i][0])

        for i in range(1, N):
            for j in range(1, M):
                cur = max(dp[i - 1][j], dp[i][j - 1])
                dp[i][j] = min(cur, nums[i][j])
        print(dp)

        print("ans: " + str(dp[N - 1][M - 1]))

s = Solution()
s.sol([[1, 2, 3],[4, 5, 1]])