class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sd={}
        td={}
        for x,y in zip(s,t):
            if x in sd:
                if sd[x]!=y:
                    return False
            else:
                sd[x]=y
            if y in td:
                if td[y]!=x:
                    return False
            else:
                td[y]=x
        return True
            