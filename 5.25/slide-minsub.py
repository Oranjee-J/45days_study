from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        total = 0
        left = 0

        ans = float('inf')

        for right in range(len(nums)):

            total += nums[right]

            while total >= target:

                ans = min(ans, right - left + 1)        # 窗口长度

                total -= nums[left]
                left += 1

        if ans == float('inf'):
            return 0

        return ans
        

s = Solution()
target = 7
nums = [2,3,1,2,4,3]

print(s.minSubArrayLen(target,nums))