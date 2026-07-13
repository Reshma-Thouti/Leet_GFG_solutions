class Solution:
    def isCycle(self, V, edges):
        parent = [i for i in range(V)]
        rank = [0 for i in range(V)]
        
        for u,v in edges:
            pu = self.find(u, parent)
            pv = self.find(v, parent)
            
            if pu == pv:
                return True
            if rank[pu] > rank[pv]:
                parent[pv] = pu
            elif rank[pv] > rank[pu]:
                parent[pu] = pv
            else:
                parent[pv] = parent[pu]
                rank[pu] += 1
        return False
                    
        # code here
    def find(self, x, parent):
        if x == parent[x]:
            return x
        parent[x] = self.find(parent[x], parent)
        return parent[x]