class Solution:
    def topoSort(self, V, edges):
        # Code here
        adj=[[] for _ in range(V)]
        inDegree=[0] * V
        for u,v in edges:
            adj[u].append(v)
            inDegree[v]+=1
        q=[]
        for i in range(V):
            if inDegree[i]==0:
                q.append(i)
        res=[]
        while q:
            node =q.pop()
            res.append(node)
            for neigh in adj[node]:
                inDegree[neigh]-=1
                if inDegree[neigh]==0:
                    q.append(neigh)
        return res