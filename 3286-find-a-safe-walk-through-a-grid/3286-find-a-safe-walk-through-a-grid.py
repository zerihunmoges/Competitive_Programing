from collections import defaultdict
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        
        m = len(grid)
        n = len(grid[0])
        visited = defaultdict(lambda: defaultdict(int))


        def isPossible(cur_x, cur_y, cur_health):
            if visited[cur_x][cur_y] >= cur_health:
                return False

            visited[cur_x][cur_y] = cur_health

            if cur_x == m-1 and cur_y == n-1:
                return True

            dirc = [[0,1], [0,-1], [1,0], [-1,0]]
            for x_dir, y_dir in dirc:

                new_x = cur_x + x_dir
                new_y = cur_y + y_dir

                if 0 <= new_x < m and 0 <= new_y < n:
                    new_health = cur_health - grid[new_x][new_y]
                    if new_health >= 1:
                        if isPossible(new_x, new_y, new_health):
                            return True

            return False

        return isPossible(0,0,health - grid[0][0])


