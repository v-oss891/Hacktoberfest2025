class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1] * m for _ in range(n)]
        def helper(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or obstacleGrid[i][j] == 1:
                return 0
            if i == n - 1 and j == m - 1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = (helper(i + 1, j) + helper(i, j + 1))
            return dp[i][j]
    
        return helper(0, 0)
