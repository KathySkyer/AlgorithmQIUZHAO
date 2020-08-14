# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。 
# 
#  找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。 
# 
#  示例: 
# 
#  X X X X
# X O O X
# X X O X
# X O X X
#  
# 
#  运行你的函数后，矩阵变为： 
# 
#  X X X X
# X X X X
# X X X X
# X O X X
#  
# 
#  解释: 
# 
#  被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被
# 填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 350 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board: return []
        n, m = len(board),len(board[0])
        def dfs(x,y):
            if x>=n or y>=m or x<0 or y<0 or board[x][y] !="O":return
            board[x][y] = "A"
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)

        for i in range(n):
            dfs(i,0)
            dfs(i,m - 1)
        for j in range(m):
            dfs(0,j)
            dfs(n - 1,j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] ="X"
                if board[i][j] =="A":
                    board[i][j] ="O"

# leetcode submit region end(Prohibit modification and deletion)
