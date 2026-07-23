class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        s1=sum(nums)
        if s1%2!=0:
            return False
        dp=[[False]*(s1+1) for i in range(n+1)]
        dp[0][0]=True
        for i in range(1,n+1):
            for j in range((s1//2)+1):
                if nums[i-1]<=j:
                    dp[i][j]= dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]
        
        return dp[n][s1//2]