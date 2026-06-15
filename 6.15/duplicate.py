class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        pos = {}

        for i, num in enumerate(nums):

            if num in pos:

                if i - pos[num] <= k:
                    return True

            pos[num] = i

        return False