
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)

        parent=[i for i in range(n)]
        dict1 = {}

        for i in range(n):
            for j in range(1, len(accounts[i])):
                email=accounts[i][j]
                if email not in dict1:
                    dict1[email]=i
                else:
                    index=dict1[email]
                    self.union(i,index,parent)
        dict2={}
        for key in dict1:
            index=self.find(dict1[key], parent)
            if index not in dict2:
                dict2[index]=[]
            dict2[index].append(key)

        result=[]
        for key in dict2:
            name=accounts[key][0]
            arr=[name]
            emails=dict2[key]
            emails.sort()
            arr.extend(emails)
            result.append(arr)
        return result
    
    def find(self, x, parent):
        if parent[x]==x:
            return x
        parent[x]=self.find(parent[x], parent)
        return parent[x]

    def union(self, x, y, parent):
        px = self.find(x, parent)
        py = self.find(y, parent)

        if px != py:
            parent[py] = px