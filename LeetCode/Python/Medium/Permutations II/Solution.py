class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # res=[]
        # def backtrack(nums,path):
        #     if len(nums)==0:
        #         if path not in res:
        #             res.append(path)
        #             return
        #         return

        #     for i in range(len(nums)):
        #         backtrack(nums[:i]+nums[i+1:],path+[nums[i]])
        # backtrack(nums,[])
        # return res
        def backtrack(i,nums,res):
            if i==len(nums)-1:
                if nums[::] not in res:
                    res.append(nums[::])
                return
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                backtrack(i+1,nums,res)
                nums[i],nums[j]=nums[j],nums[i]
        res=[]
        backtrack(0,nums,res)
        return res