'''
205. 同构字符串
已解答
简单
相关标签
premium lock icon
相关企业
给定两个字符串 s 和 t ，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
'''



class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for c1,c2 in zip(s,t):

            if c1 in s_to_t:
                if s_to_t[c1] != c2:
                    return False
            
            if c2 in t_to_s:
                if t_to_s[c2] != c1:
                    return False


            s_to_t[c1] = c2
            t_to_s[c2] = c1

        return True


r = Solution()

s = "egg"
t = "add"

print(r.isIsomorphic(s,t))