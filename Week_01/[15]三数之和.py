# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例： 
# 
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#  
#  Related Topics 数组 双指针 
#  👍 2387 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        """
        n = len(nums)
        res =[]
        if (not nums or n<3):
            return res
        nums.sort()
        for i in range(n):
            if nums[i] > 0 :
                return res
            if i>0 and nums[i]==nums[i-1]:
                continue
            L=i+1
            R=n-1
            while L<R:
                if nums[L] +nums[R] + nums[i] == 0 :
                    res.append([nums[i],nums[L],nums[R]])
                    while (L<R) and nums[L]==nums[L+1]:
                        L += 1
                    while (L<R) and nums[R]==nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
                elif nums[R] +nums[L] +nums[i] > 0:
                    R -= 1
                else:
                    L += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)
