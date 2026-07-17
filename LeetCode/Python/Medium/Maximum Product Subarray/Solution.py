class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp=nums[0]
        minp=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                maxp,minp=minp,maxp
            maxp=max(nums[i],nums[i]*maxp)
            minp=min(nums[i], nums[i]*minp)
            res=max(res,maxp)
        return res
        