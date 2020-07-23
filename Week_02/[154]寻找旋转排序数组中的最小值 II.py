# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。 
# 
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
# 
#  请找出其中最小的元素。 
# 
#  注意数组中可能存在重复的元素。 
# 
#  示例 1： 
# 
#  输入: [1,3,5]
# 输出: 1 
# 
#  示例 2： 
# 
#  输入: [2,2,2,0,1]
# 输出: 0 
# 
#  说明： 
# 
#  
#  这道题是 寻找旋转排序数组中的最小值 的延伸题目。 
#  允许重复会影响算法的时间复杂度吗？会如何影响，为什么？ 
#  
#  Related Topics 数组 二分查找 
#  👍 141 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        """
        if not nums: return []
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        return nums[0]
        # 二分法
        # if not nums: return 0
        # for i in range(len(nums) - 1):
        #     if nums[i] > nums[i + 1]:
        #         return nums[i + 1]
        # return nums[0]
        # if not nums: return 0
        # l = 0
        # r = len(nums) - 1
        # while l<r:
        #     mid = (l + r )/2
        #     if nums[mid] > nums[r]:
        #         l = mid + 1
        #     else:
        #         r = mid
        # return nums[l]
        # 直接调用python封装好的min函数（时间复杂度有点高）
        # return min(nums)
# leetcode submit region end(Prohibit modification and deletion)
q=Solution()
a = q.findMin([3,3,1,3])
print(a)