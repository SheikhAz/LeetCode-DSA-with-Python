class Solution(object):
    def orangesRotting(self, grid):
        row = len(grid)
        col = len(grid[0])
        grid_copy = deepcopy(grid)
        queue = deque()
        fresh = 0
        for r in range(row):
            for c in range(col):
                if grid_copy[r][c] == 2:
                    queue.append((r,c))
                elif grid_copy[r][c] == 1:
                    fresh += 1
        minute = 0
        while len(queue) != 0 and fresh > 0:
            minute += 1
            rotten = len(queue)
            for _ in range(rotten):
                r , c = queue.popleft()
                for i , j in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_i = r + i
                    new_j = c + j
                    if new_i < 0 or new_i==row or new_j < 0 or new_j == col:
                        continue
                    if grid_copy[new_i][new_j] == 2 or grid_copy[new_i][new_j] == 0:
                        continue
                    fresh -= 1
                    grid_copy[new_i][new_j] = 2
                    queue.append((new_i,new_j))
        if fresh > 0:
            return -1
        return minute


        