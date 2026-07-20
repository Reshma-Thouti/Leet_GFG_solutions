class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        for i in range(len(s)):
            if s[i] in d and d[s[i]]!=t[i]:
                return False
            if s[i] not in d:
                d[s[i]]=t[i]
        return True
            