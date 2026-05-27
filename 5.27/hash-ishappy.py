class Solution:
    def isHappy(self, n: int) -> bool:

        all = set()
        while n != 1:
            if n in all:
                return False

            all.add(n)

            total = 0

            while n > 0:
                digit = n%10
                total = total + digit * digit

                n = n//10
            
            n = total

        return True