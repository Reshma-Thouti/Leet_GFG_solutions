class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        nc=numCourses
        c=[[] for _ in range(nc)]
        id=[0]*nc

        for u,v in prerequisites:
            c[u].append(v)
            id[u]+=1
        q=[]
        for i in range(nc):
            if id[i]==0:
                q.append(i)
        if not q:
            return False
        # while q:
        #     mc+=1

        #     for _ in range(len(q)):
        #         ele=q.pop(0)
        #         for e in c[ele]:
        #             if id[ele]==0:
        #                 id[e]-=1
        #                 q.append(e)
        return True

        

            
            