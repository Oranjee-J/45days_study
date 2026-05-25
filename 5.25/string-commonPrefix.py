'''
14. 最长公共前缀
已解答
简单
相关标签
premium lock icon
相关企业
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
 

'''



from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        pre = ''

        n = len(strs[0])

        for ch in strs:
            n = min(n,len(ch))      # 找到长度最小的字符串，设定边界避免非法索引

        # print(n)
        flag = n
        for i in range(0,len(strs)-1):

            for j in range(0,n):
                if strs[i][j] != strs[i+1][j]:

                    flag = min(flag,j)
                    break

        for i in range(0,flag):
            pre += strs[0][i]

        return pre
    

s = Solution()
strs = ["flower","flow","flight"]

print(s.longestCommonPrefix(strs))