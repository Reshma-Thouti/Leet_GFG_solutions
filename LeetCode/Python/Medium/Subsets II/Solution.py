class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curr=[]
        res=[]
        nums.sort()
        self.bt(0,nums,curr,res)
        return res
    def bt(self, i,nums, curr, res):
        res.append(curr[:]) 
        if i>=len(nums):
            return
        for j in range(i,len(nums)):
            if j>i and nums[j]==nums[j-1]:
                continue
            curr.append(nums[j])
            self.bt(j+1,nums,curr,res)
            curr.pop()