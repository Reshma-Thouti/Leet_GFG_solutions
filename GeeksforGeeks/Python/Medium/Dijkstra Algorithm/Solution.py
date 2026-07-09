import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        adjList = []
        for i in range(V):
            adjList.append([])
        
        for edge in edges:
            u, v, w = edge
            adjList[u].append([v, w])
            adjList[v].append([u, w])
        dist=[float('inf')]*V
        dist[src] = 0
        queue=[]
        heapq.heappush(queue, (0, src))
        while queue:
            curr = heapq.heappop(queue)
            weight = curr[0]
            node = curr[1]
            
            if weight>dist[node]:
                continue
            for neighbor in adjList[node]:
                neighNode = neighbor[0]
                neighWeight = neighbor[1]
                
                if weight + neighWeight < dist[neighNode]:
                    dist[neighNode] = weight + neighWeight
                    heapq.heappush(queue, (dist[neighNode], neighNode))
        return dist