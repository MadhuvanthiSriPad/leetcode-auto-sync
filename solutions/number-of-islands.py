class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid) , len(grid[0])
        islands=0
        visited=set()

        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1" and (r,c) not in visited:
                    q = deque([(r,c)])
                    visited.add((r,c))
                    islands+=1
                while q:
                    dr,dc = q.popleft()
                    for nr , nc in ([-1,0],[0,-1],[1,0],[0,1]):
                        newr,newc = dr+nr,dc+nc
                        if(0<=newr<row and 0<=newc<col and (newr,newc) not in visited and grid[newr][newc]=="1"):
                            visited.add((newr,newc))
                            q.append((newr,newc))
        return islands



        