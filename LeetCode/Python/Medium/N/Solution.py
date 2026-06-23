"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
         #iterative approch
        if root==None:
            return []
        d=deque([root])
        res=[]
        while d!=deque():
            l=[]
            for i in range(len(d)):
                node=d.popleft()
                l.append(node.val)
                for child in node.children:
                    d.append(child)
            res.append(l)
        return res


        """
        if not root:
            return []
        q=deque([[root]]) # q[root]  # q=[[root],[3,4,5]]   nums=[10,20,30]
        res=[[root.val]]
        while q:
            l=[]
            ql=[]
            nodes=q.popleft() #nodes=root  [10,20,30]
            for node in nodes:
                for child in node.children:
                    ql.append(child)
                    l.append(child.val)
            if l:
                    res.append(l[:])
                    q.append(ql)
        return res