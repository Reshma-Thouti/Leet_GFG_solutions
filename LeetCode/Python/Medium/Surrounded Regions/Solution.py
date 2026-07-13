class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q=[]
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="-1"
                    q.append([i,j])
        c=0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for _ in range(len(q)):
            r,c=q.pop(0)
            
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0<=nr<m and 0<=nc<n:
                    if board[nr][nc]=="-1" or board[nr][nc]=="O":
                        board[r][c]="O"
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="-1":
                    board[i][j]="O"

        