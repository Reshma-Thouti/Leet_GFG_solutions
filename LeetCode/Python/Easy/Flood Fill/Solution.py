class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        x=image[sr][sc]
        if x==color:
            return image
        self.bfs(image, x, color, sr, sc)
        return image

    def bfs(self, image, x, color, sr, sc):
        m=len(image)
        n=len(image[0])
        
        if sr < 0 or sr >= m or sc <0 or sc >= n:
            return
        if image[sr][sc]!=x:
            return
        if image[sr][sc]==x:
            image[sr][sc]=color 
            self.bfs(image, x, color, sr-1,sc)
            self.bfs(image, x, color, sr,sc-1)
            self.bfs(image, x, color, sr+1,sc)
            self.bfs(image, x, color, sr,sc+1)