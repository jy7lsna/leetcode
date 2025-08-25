class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        ROWS, COL = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COL or grid [r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(ROWS):
            for c in range(COL):
                if grid[r][c] == "1":
                    count += 1 
                    dfs(r,c)
        return count

