class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        f=Counter(answers)
        res=0
        for i,c in f.items():
            x=(c+i)//(i+1)
            res+=(i+1)*x
        return res

