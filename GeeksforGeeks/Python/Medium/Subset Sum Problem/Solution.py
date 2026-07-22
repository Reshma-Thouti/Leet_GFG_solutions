class Solution:
    # def solve(self, n, sum, arr,dp):
    #     if sum==0:
    #         return True
    #     if n==0:
    #         if arr[0]==sum:
    #             return True
    #         return False
            
    #     if dp[n][sum]!=-1:
    #         return dp[n][sum]
        
    #     notPick=self.solve(n-1, sum,arr,dp)
    #     pick=False
    #     if arr[n]<=sum:
    #         pick=self.solve(n-1, sum-arr[n],arr,dp)
        
    #     dp[n][sum]=pick or notPick
    #     return dp[n][sum]
        
    def isSubsetSum (self, arr, sum):
        n=len(arr)
        dp=[[False]*(sum+1) for i in range(n+1)]
        # return self.solve(n-1, sum, arr,dp)
        for i in range(n + 1):
            dp[i][0] = True
        
        for i in range(1,n+1):
            for j in range(1,sum+1):
                if arr[i-1]<=j:
                    dp[i][j]=dp[i-1][j] or  dp[i-1][j-arr[i-1]] 
                else:
                    dp[i][j]=dp[i-1][j]
        
        return dp[n][sum]
        