class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        cp=pairs[0]
        c=0
        for i in range(1,len(pairs)):
            if pairs[i][0]>cp[1]:
                cp=pairs[i]
                c+=1
        return c+1