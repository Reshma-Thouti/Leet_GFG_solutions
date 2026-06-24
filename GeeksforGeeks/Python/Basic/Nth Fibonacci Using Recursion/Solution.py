class Solution:
    def nthFibonacci(self, n):
        # Code here
        if n==0 or n==1:
            return n
        p1=0
        p2=1
        num=p1+p2
        def fun(n,num,p1,p2):
            if n==0:
                return num
            return fun(n-1,p2+num,p2,num)
        return fun(n-2,num,p1,p2)