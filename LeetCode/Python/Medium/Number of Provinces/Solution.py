class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        p = [i for i in range(n)]
        r = [0] * n
        c = n

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    if self.uni(i, j, p, r):
                        c -= 1

        return c

    def find(self, x, p):
        if p[x] != x:
            p[x] = self.find(p[x], p) 
        return p[x]

    def uni(self, x, y, p, r):
        px = self.find(x, p)
        py = self.find(y, p)

        if px == py:
            return False

        if r[px] > r[py]:
            p[py] = px
        elif r[px] < r[py]:
            p[px] = py
        else:
            p[py] = px
            r[px] += 1

        return True