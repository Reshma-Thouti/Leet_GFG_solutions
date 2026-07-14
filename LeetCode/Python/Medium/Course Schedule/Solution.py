from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        c = [[] for _ in range(numCourses)]
        id = [0] * numCourses

        for u, v in prerequisites:
            if u == v:
                return False
            c[v].append(u)      # reverse edge
            id[u] += 1          # indegree of u

        q = deque()

        for i in range(numCourses):
            if id[i] == 0:
                q.append(i)

        mc = 0

        while q:
            ele = q.popleft()
            mc += 1

            for e in c[ele]:
                id[e] -= 1
                if id[e] == 0:
                    q.append(e)

        return mc == numCourses