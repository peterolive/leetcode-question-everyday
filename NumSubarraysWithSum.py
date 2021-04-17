from typing import List


class NumSubarraysWithSum:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        map_ = {}
        pre_sum = 0
        res = 0

        map_[pre_sum] = 1

        for num in A:
            pre_sum += num
            print("pre_sum", pre_sum, "pre_sum - S", pre_sum - S)
            if map_.get(pre_sum - S):
                res += map_.get(pre_sum - S)
            print(map_)
            map_[pre_sum] = map_.get(pre_sum, 0) + 1

            print(res)

        return res
