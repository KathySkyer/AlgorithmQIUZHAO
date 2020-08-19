# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  示例 1: 
# 
#  输入: ["flower","flow","flight"]
# 输出: "fl"
#  
# 
#  示例 2: 
# 
#  输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#  
# 
#  说明: 
# 
#  所有输入只包含小写字母 a-z 。 
#  Related Topics 字符串 
#  👍 1221 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if not strs or len(strs) == 0 : return ""
        # for i in range(len(strs[0])):
        #     c = strs[0][i]
        #     for j in range(1,len(strs)):
        #         if i == len(strs[j]) or strs[j][i] != c :
        #             return strs[0][0:i]
        # return strs[0]
        if not strs or len(strs) == 0 : return ""
        str0,str1 = min(strs),max(strs)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[0:i]
        return str0



# leetcode submit region end(Prohibit modification and deletion)
q=Solution()
a = q.longestCommonPrefix(["flower","flow","flight"])
print(a)