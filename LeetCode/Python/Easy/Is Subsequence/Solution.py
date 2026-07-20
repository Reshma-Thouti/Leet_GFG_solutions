class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls=len(s)
        lt=len(t)
        j=0
        if ls>lt:
            for i in range(ls):
                if s[i]==t[j]:
                    j+=1
        else:
            for i in range(lt):
                if s[j]==t[i]:
                    j+=1
        return j==min(ls,lt)

