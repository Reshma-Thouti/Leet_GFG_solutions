class Solution:
    def perfectSum(self, arr, target):
        # code here
        n=len(arr)
        dp=[[0]*(target+1) for _ in range(n+1)]
        dp[0][0]=1
        for i in range(1, n+1):
            for j in range(target+1):
                if arr[i-1]<=j:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-arr[i-1]]
                    
                else:
                    dp[i][j]=dp[i-1][j]
        
        return dp[n][target]