from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum_to_times = {0: 1}
        pre_sum = 0
        res = 0

        for num in nums:
            pre_sum += num
            if pre_sum - k in pre_sum_to_times:
                res += pre_sum_to_times[pre_sum - k]

            pre_sum_to_times[pre_sum] = pre_sum_to_times.get(pre_sum, 0) + 1

        return res
#  k = 2
# [1,-1,3,-3,2]
# pre_sum1 = 1 + -1 = 0
# pre_sum2 = 1 + -1 + 3 + -3 = 0
# pre_sum3 = 1 + -1 + 3 + -3 + 2 = 2
#
# 0 本身开始就有一次加上之后的两次就是三次
# 因为  pre_sum3 - pre_sum1 = 2 说明 [1,-1,3,-3,2] 去掉 [1,-1]，剩下的[3,-3,2]是连续的，等于2
#     pre_sum3 - pre_sum2 = 2 说明 [1,-1,3,-3,2] 去掉 [1,-1, 3, -3]，剩下的[2]是连续的，等于2
# 第一次是本身其实可以想做 [1,-1,3,-3,2] - []，剩下的 [1,-1,3,-3,2] 是连续的，等于2
# 一开始要给 {0：1}，是因为会出现[1,-1,3,-3,2] - []，会有减去一个空集的情况，前面没有东西可以拿来 - ，就像[2] - []，当k=2的时候。
# pre_sum减去空集等于k的情况。
# 剩下的 [1,-1,3,-3,2] 是连续的，等于2的情况


