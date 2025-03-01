class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:
            return -1
        fresh,mins=0,0
        row,col=len(grid),len(grid[0])
        q=deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2 :
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        if fresh==0:
            return 0
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]

        while q:
            for _ in range(len(q)):
                dr,dc = q.popleft()
                for i,j in dirs:
                    nr,nc = dr+i,dc+j

                    if ( 0<=nr<row and 0<=nc<col and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        q.append((nr,nc))
                        fresh-=1
            mins+=1

        return mins-1 if fresh==0 else -1