
        parent = [i for i in range(V)]
        rank = [0] * V

        cost = 0
        count = 0

        for u, v, w in edges:
            if self.union(u, v, parent, rank):
                cost += w
                count += 1

            if count == V - 1:
                break

        return cost

    def find(self, x, parent):
        if parent[x] != x:
            parent[x] = self.find(parent[x], parent)
        return parent[x]

    def union(self, x, y, parent, rank):
        px = self.find(x, parent)
        py = self.find(y, parent)

        if px == py:
            return False

        if rank[px] < rank[py]:
            parent[px] = py
        elif rank[px] > rank[py]:
            parent[py] = px
        else:
            parent[py] = px
            rank[px] += 1

        return True