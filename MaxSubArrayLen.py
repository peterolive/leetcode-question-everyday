class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        pre_sum_to_index = {0: -1}
        res = 0
        pre_sum = 0
        n = len(nums)

        for i in range(n):
            pre_sum += nums[i]
            if pre_sum - k in pre_sum_to_index:
                res = max(res, i - pre_sum_to_index[pre_sum - k])
            if pre_sum not in pre_sum_to_index:
                pre_sum_to_index[pre_sum] = i

        return res
