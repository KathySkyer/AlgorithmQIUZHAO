# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre,cur = 0,1
        while cur < len(nums):
            if nums[pre] == nums[cur]:
                nums.pop(cur)
            else:
                pre = pre + 1
                cur = cur + 1
        return len(nums)