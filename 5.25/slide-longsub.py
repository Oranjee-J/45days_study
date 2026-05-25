class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()

        left = 0
        ans = 0

        for right in range(len(s)):

            # 如果重复
            while s[right] in window:

                # 左边不断缩小窗口
                window.remove(s[left])
                left += 1

            # 加入当前字符
            window.add(s[right])

            # 更新最大长度
            ans = max(ans, right - left + 1)

        return ans


test = Solution()
s = "abcabcbb"
print(test.lengthOfLongestSubstring(s))