'''
209. 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0 

'''


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