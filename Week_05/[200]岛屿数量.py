# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1: 
# 
#  输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 706 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # dfs
    #     if len(grid) == 0:return 0
    #     n,m = len(grid),len(grid[0])
    #     num_grigd =0
    #     for  i in range(n):
    #         for j in range(m):
    #             if grid[i][j] =="1":
    #                 num_grigd+=1
    #                 self.dfs(grid,i,j)
    #     return num_grigd
    # def dfs(self, grid, r, c):
    #     grid[r][c]=0
    #     nr, nc = len(grid), len(grid[0])
    #     for x,y in [(r-1,c),(r,c - 1),(r + 1,c),(r,c + 1)]:
    #         if 0<=x<nr and 0 <=y <nc and grid[x][y] =="1":
    #             self.dfs(grid,x,y)

        res, f = set(), {}
        def find(x):
            f.setdefault(x,x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]
        def union(x,y):
            f[find(x)] = find(y)

        if len(grid) == 0: return 0
        n,m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    for x,y in [[-1,0],[0,-1]]:
                        tmp_i = i + x
                        tmp_j = j + y
                        if 0 <= tmp_i <n and 0 <=tmp_j <m and grid[tmp_i][tmp_j] =="1":
                            union(tmp_i * n +tmp_j, i * n + j)

        for i in range(n):
            for j in range(m):
                if grid[i][j] =="1":
                    res.add(find((i*n+j)))
        return len(res)






# leetcode submit region end(Prohibit modification and deletion)
q=Solution()
a  = q.numIslands([['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']])
print(a)