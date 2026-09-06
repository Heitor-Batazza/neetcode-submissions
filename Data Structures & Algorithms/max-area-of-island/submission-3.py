class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:        
        max_island = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            island_length = 1
            q = collections.deque()
            q.append((r, c))
            grid[r][c] = 0

            while q:
                row, col = q.popleft()
                for (dr, dc) in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        q.append((r, c))
                        island_length += 1
                        grid[r][c] = 0
            return island_length

        for r in range(rows):
            for c in range (cols):
                if grid[r][c] == 1:
                    max_island = max(max_island, bfs(r, c))

        return max_island
        


        
        