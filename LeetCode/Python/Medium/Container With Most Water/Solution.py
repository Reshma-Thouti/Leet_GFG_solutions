class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        n=len(height)
        r=n-1
        res=0
        while l<r:
            if height[l]>=height[r]:
                res=max(res, (r-l)*height[r])
                r-=1
            elif height[l]<height[r]:
                res=max(res, (r-l)*height[l])
                l+=1
        return res