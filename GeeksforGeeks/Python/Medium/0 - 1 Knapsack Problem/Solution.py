class Solution:
    # def solve(self, n, W, val, wt, dp):
    #     if n==0:
    #         if wt[0]<=W:
    #             return val[0]
    #         return 0
    #     if dp[n][W]!=-1:
    #         return dp[n][W]
    #     notPick=self.solve(n-1,W,val,wt,dp)
    #     pick=0
    #     if wt[n]<=W:
    #         pick=val[n]+self.solve(n-1, W-wt[n], val, wt, dp)
        
    #     dp[n][W]=max(notPick, pick)
    #     return dp[n][W]
        
    def knapsack(self, W, val, wt):
        n=len(val)
        dp=[[0]*(W+1) for i in range(n+1)]
        # return self.solve(n-1, W, val, wt, dp)
        for i in range(1,n+1):
            for j in range(W+1):
                if wt[i-1]<=j:
                    dp[i][j]=max(dp[i-1][j], val[i-1]+dp[i-1][j-wt[i-1]])
                else:
                    dp[i][j]=dp[i-1][j]
        
        return dp[n][W]
                
        
