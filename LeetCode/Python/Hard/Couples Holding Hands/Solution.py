class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        c=0
        for i in range(0,len(row),2):
            if row[i]%2!=0:
                if row[i+1]+1!=row[i]:
                    j=i+1
                    while j<len(row) and row[j]!=row[i]-1:
                        j+=1
                    row[i+1],row[j]=row[j],row[i+1]
                    c+=1
            else:
                if row[i+1]-1!=row[i]:
                    j=i+1
                    while j<len(row) and row[j]!=row[i]+1:
                        j+=1
                    row[i+1],row[j]=row[j],row[i+1]
                    c+=1
        return c