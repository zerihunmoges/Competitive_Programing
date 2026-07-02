from collections import deque
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        


        dirc = [[0,1], [0,-1], [1,0], [-1,0]]
        m = len(grid)
        n = len(grid[0])
        visited = set()

        cells = deque([[0,0, health-grid[0][0]]])

        while cells:
            cur_x, cur_y, cur_health = cells.popleft()
            if (cur_x, cur_y, cur_health) in visited:
                continue

            visited.add((cur_x, cur_y, cur_health))

            if cur_x == m-1 and cur_y == n-1:
                return True

            for x_dir, y_dir in dirc:

                new_x = cur_x + x_dir
                new_y = cur_y + y_dir

                if 0 <= new_x < m and 0 <= new_y < n:
                    new_health = cur_health - grid[new_x][new_y]
                    if new_health >= 1:
                        cells.append([new_x, new_y, new_health])

        return False


