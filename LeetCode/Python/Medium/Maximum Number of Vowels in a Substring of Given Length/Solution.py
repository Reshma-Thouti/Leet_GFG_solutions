from collections import deque
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if len(s)<k:
            return 0
        res=0
        c=0
        ns=deque()
        for ch in s:
            if len(ns)==k:
                if ns[0] in 'aeiou':
                    c-=1
                ns.popleft()
            if ch in 'aeiou':
                c+=1
            ns.append(ch)
            res=max(res, c)
        return res
                    