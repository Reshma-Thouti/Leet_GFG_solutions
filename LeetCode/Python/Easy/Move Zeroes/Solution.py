class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=-1
        n=len(nums)
        for i in range(0,n):
            if j==-1 and nums[i]==0:
                j=i
            if j!=-1 and i!=j and nums[i]!=0:
                nums[i], nums[j]=nums[j],nums[i]
                j+=1
            
        
                


