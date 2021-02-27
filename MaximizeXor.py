from typing import List


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums = sorted(nums)
        queries = sorted(((i, x, mi) for i, x, mi in enumerate(queries)), key=lambda x: x[2])
        res = [0] * len(queries)

        for k in range(32, -1, -1):
            prefixes = set()

            j = 0

            for i, x, mi in queries:
                while j < len(nums) and nums[j] <= mi:
                    prefixes.add(nums[j] >> k)
                    j += 1
                if not prefixes:
                    res[i] = -1
                else:
                    res[i] <<= 1
                    target = res[i] ^ 1
                    if (x >> k) ^ target in prefixes:
                        res[i] = target

        return res
