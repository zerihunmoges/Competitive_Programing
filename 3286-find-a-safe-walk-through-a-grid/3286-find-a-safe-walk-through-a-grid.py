import heapq
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        


        dirc = [[0,1], [0,-1], [1,0], [-1,0]]
        m = len(grid)
        n = len(grid[0])
        visited = set()

        cells = [[-(health-grid[0][0]), 0,0]]

        while cells:
            cur_health , cur_x, cur_y = heapq.heappop(cells)
            cur_health*=-1
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
                        heapq.heappush(cells, [-new_health, new_x, new_y])

        return False


