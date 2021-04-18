from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most(k):
            left = 0
            ans = 0
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    k -= 1
                while k < 0:
                    k += nums[left] % 2
                    left += 1
                ans += left - right + 1
            return ans

        return at_most(k) - at_most(k - 1)
