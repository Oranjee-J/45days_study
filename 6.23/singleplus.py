class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        # int 是 32 位
        for i in range(32):

            cnt = 0

            for num in nums:
                cnt += (num >> i) & 1

            if cnt % 3:
                ans |= (1 << i)

        # 处理负数
        if ans >= 2 ** 31:
            ans -= 2 ** 32

        return ans