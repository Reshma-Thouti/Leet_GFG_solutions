class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        s=x
        n=0
        while x!=0:
            n=n*10+x%10
            x//=10
        if s==n:
            return True
        return False
        