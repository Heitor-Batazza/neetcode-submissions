class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        dist = 1
        

        def add(r, c):
            if r in range(rows) and c in range(cols) and (r, c) not in visit and grid[r][c] == 2147483647:
                grid[r][c] = dist
                q.append((r, c))
                visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)
            dist += 1




        