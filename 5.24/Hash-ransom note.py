'''

383. 赎金信

给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
如果可以，返回 true ；否则返回 false 。
magazine 中的每个字符只能在 ransomNote 中使用一次。

示例 1：
    输入：ransomNote = "a", magazine = "b"
    输出：false

示例 2：
    输入：ransomNote = "aa", magazine = "ab"
    输出：false

示例 3：
    输入：ransomNote = "aa", magazine = "aab"
    输出：true
 
提示：
1 <= ransomNote.length, magazine.length <= 105 ransomNote 和 magazine 由小写英文字母组成


'''







from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = defaultdict(int)
        for c in magazine:
            count[c] += 1

        count_r =  defaultdict(int)
        for d in ransomNote:
            count_r[d] += 1


        for key in count_r.keys():
            if count[key] < count_r[key]:
                return False

        return True
    

s = Solution()
ransomNote = "aa"
magazine = "ab"

print(s.canConstruct(ransomNote, magazine))