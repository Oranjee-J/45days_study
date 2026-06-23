class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:

            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            # 当前位
            res.append(str(total % 2))

            # 更新进位
            carry = total // 2

        # 因为是从低位到高位加入，需要翻转
        return ''.join(res[::-1])