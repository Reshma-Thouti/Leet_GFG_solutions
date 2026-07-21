class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        # if n<=1:
        #     return float(nums[0])
        # s=0
        # res=0
        # for i in range(n-k+1):
        #     s=sum(nums[i:i+k])
        #     res=max(res, s/k)
        # return res

        s=sum(nums[:k])
        res=s/k
        for i in range(k,n):
            s=s-nums[i-k]+nums[i]
            res=max(res, s/k)
        return res