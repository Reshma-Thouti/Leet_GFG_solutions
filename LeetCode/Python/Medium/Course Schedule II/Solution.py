class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nc=numCourses
        c=[[] for _ in range(nc)]
        id=[0]*nc
        for u,v in prerequisites:
            c[v].append(u)
            id[u]+=1
        q=deque()
        for i in range(nc):
            if id[i]==0:
                q.append(i)
        res=[]
        mc=0
        while q:
            node=q.popleft()
            mc=0
            res.append(node)
            for ele in c[node]:
                id[ele]-=1
                if id[ele]==0:
                    q.append(ele)
        return res