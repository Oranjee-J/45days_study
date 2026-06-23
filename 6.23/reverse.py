class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):
            # 给结果腾出一位
            res <<= 1

            # 将 n 的最低位加入 res
            res |= (n & 1)

            # n 右移
            n >>= 1

        return res