# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
#  Related Topics 数组 动态规划 
#  👍 692 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return nums
        pre_max= pre_min=res=nums[0]
        for i in nums[1:]:
            cur_max = max(pre_max * i, pre_min * i, i)
            cur_min = min(pre_max * i, pre_min * i, i)
            res = max(res,cur_max)
            pre_min = cur_min
            pre_max = cur_max
        return res

# leetcode submit region end(Prohibit modification and deletion)
