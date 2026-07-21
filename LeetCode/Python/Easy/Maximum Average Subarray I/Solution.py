class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        s=0
        res=0
        for i in range(n-k+1):
            s=sum(nums[i:i+k])
            res=max(res, s/k)
        return res