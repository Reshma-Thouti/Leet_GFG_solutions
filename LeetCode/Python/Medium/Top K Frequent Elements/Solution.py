class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        nd=dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
        res=[]
        for num in nd:
            if len(res) == k:
                break
            res.append(num)
        return res

