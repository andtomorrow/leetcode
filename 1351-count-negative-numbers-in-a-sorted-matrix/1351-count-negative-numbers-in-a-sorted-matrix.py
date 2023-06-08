class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        s_y, s_x = 0, 0

        neg_nums = 0

        grid = grid[::-1]


        for i in range(s_y, m):
            for j in range(s_x, n):
                if grid [i][j] < 0:
                    neg_nums += n - j
                    break

        return neg_nums