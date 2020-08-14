# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。 
# 
#  示例: 
# 
#  输入: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# 输出: 4 
#  Related Topics 动态规划 
#  👍 509 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 二维dp
        # if len(matrix) == 0 or len(matrix[0]) == 0:
        #     return 0
        # n, m,maxside = len(matrix),len(matrix[0]), 0
        # dp = [[0] * m for _ in range(n)]
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j] == "1":
        #             if i == 0 or j == 0:
        #                 dp[i][j] = 1
        #             else:
        #                 dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i -1][j - 1]) +1
        #             maxside = max(maxside, dp[i][j])
        # return maxside*maxside

        nums = [int(''.join(n),base = 2) for n in matrix]
        res,n = 0,len(nums)
        for i in range(n):
            tmp = nums[i]
            for j in range(i,n):
                tmp &= nums[j]
                w = self.getwith(tmp)
                res = max(res, min(w , j-i+1))
        return res*res
    def getwith(self, nums):
        w = 0
        while nums>0:
            nums &= nums<<1
            w +=1
        return w



# leetcode submit region end(Prohibit modification and deletion)
q=Solution()
a = q.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
print(a)