'''

42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
                     __
         __         |  |__    __
   __   |  |__    __|  |  |__|  |__
__|__|__|__|__|__|__|__|__|__|__|__|
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
'''

class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        if n == 0:
            return 0

        # 左边最大高度
        left_max = [0] * n

        # 右边最大高度
        right_max = [0] * n

        # 构建 left_max
        left_max[0] = height[0]

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # 构建 right_max
        right_max[n - 1] = height[n - 1]

        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        # 计算雨水
        rain = 0

        for i in range(n):
            rain += min(left_max[i], right_max[i]) - height[i]

        return rain