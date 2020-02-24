class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(row, col, x, y):
            if grid[x][y] == "0":
                return
            grid[x][y] = "0"
            if x != 0:
                dfs(row, col, x-1, y)
            if x != row-1:
                dfs(row, col, x+1, y)
            if y != 0:
                dfs(row, col, x, y-1)
            if y != col-1:
                dfs(row, col, x, y+1)
        if not grid:
            return 0
        num_rol = len(grid)
        num_col = len(grid[0])
        count = 0
        for rol in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[rol][col] == "1":
                    dfs(num_rol,num_col,rol,col)
                    count += 1
        return count