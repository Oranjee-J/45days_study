'''
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。
数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。

 

'''


class Solution:
    def romanToInt(self, s: str) -> int:
        total =0

        roman_map = {"I": 1, "V": 5, "X":10, "L":50, "C": 100, "D":500, "M": 1000}

        for i in range(0,len(s)):
            if i < len(s)-1:
                if roman_map[s[i]]<roman_map[s[i+1]]:
                    total = total - roman_map[s[i]]
                else:
                    total = total + roman_map[s[i]]
            else:
                total = total + roman_map[s[i]]
        
        return total