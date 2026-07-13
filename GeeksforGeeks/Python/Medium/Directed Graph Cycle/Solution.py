class Solution:
    def isCyclic(self, V, edges):
        # code here
        adj=[[] for _ in range(V)]
        path=[False] * V
        visited=[False] * (V)
        for u,v in edges:
            adj[u].append(v)
        for  i in range(V):
            if not visited[i]:
                if self.cycle(adj,visited,i,path):
                    return True
        return False
    def cycle(self,adj,visited,node,path):
        visited[node]=True
        path[node]=True
        for neigh in adj[node]:
            if  not visited[neigh]:
                if self.cycle(adj,visited,neigh,path):
                    return True
            elif path[neigh]:
                return True
        path[node]=False
        return False