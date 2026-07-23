class Solution:
    def permutations(self, res, s1,i):
            if i==len(s1):
                res.append("".join(s1))
                return
            for j in range(i,len(s1)):
                s1[i],s1[j]=s1[j],s1[i]
                self.permutations(res, s1, j+1)
                s1[i],s1[j]=s1[j],s1[i]
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=list(s1)
        res=[]
    
        self.permutations(res,s1, 0)

        for i in range(len(res)):
            if res[i] in s2:
                return True
        return False
