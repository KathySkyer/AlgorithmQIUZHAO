# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。 
# 
#  说明：本题中，我们将空字符串定义为有效的回文串。 
# 
#  示例 1: 
# 
#  输入: "A man, a plan, a canal: Panama"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "race a car"
# 输出: false
#  
#  Related Topics 双指针 字符串 
#  👍 264 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # news = re.sub('[\W_]+', '', s).lower()
        # revers = news[::-1]
        # if news == revers:
        #     return True
        # else:
        #     return False
        # s = ''.join(filter(str.isalnum, s.lower()))
        # return s == s[::-1]

        news = ""
        for i in s:
            if i.isalnum():
                i = i.lower()
                news += "".join(i)
        i, j = 0,len(news) - 1
        while i<j:
            if news[i] != news[j]:
                return False
            i+=1
            j-=1
        return True
        # return news == news[::-1]


# leetcode submit region end(Prohibit modification and deletion)
