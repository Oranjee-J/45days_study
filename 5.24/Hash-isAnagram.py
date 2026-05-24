'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。

 

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
 

提示:

1 <= s.length, t.length <= 5 * 104
s 和 t 仅包含小写字母

'''


from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst_s = list(s)
        lst_t = list(t)
        count_s = defaultdict(int)
        count_t = defaultdict(int)

        for c1 in lst_s:
            count_s[c1] += 1

        for c2 in lst_t:
            count_t[c2] += 1

        
        for i in count_s.keys():
            if count_s[i] != count_t[i]:
                return False
            
        for j in count_t.keys():
            if count_s[j] != count_t[j]:
                return False
            
        
        return True
    

end = Solution()

s = "anagram"
t = "nagaram"

print(end.isAnagram(s,t))