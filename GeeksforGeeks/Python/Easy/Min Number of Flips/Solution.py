class Solution:
    def minFlips(self, s):
        # Code here
        f1=0
        f2=0
        for i in range(len(s)):
            if int(s[i])==(i)%2:
                f2+=1
            if int(s[i])==(i+1)%2:
                f1+=1
        return min(f1,f2)
                
                
                
                    
