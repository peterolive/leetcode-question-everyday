from typing import List
# merge sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = [0 for _ in range(n)]
        self.merge_sort(nums, temp, 0, n - 1)

        return nums

    def merge_sort(self, nums, temp, start, end):
        if start >= end:
            return

        mid = start + (end - start) // 2
        self.merge_sort(nums, temp, start, mid)
        self.merge_sort(nums, temp, mid + 1, end)
        self.merge(start, end, nums, temp)

    def merge(self, start, end, nums, temp):
        mid = start + (end - start) // 2
        left, right = start, mid + 1
        index = start

        while left <= mid and right <= end:
            if nums[left] <= nums[right]:
                temp[index] = nums[left]
                left += 1
            else:
                temp[index] = nums[right]
                right += 1
            index += 1

        while left <= mid:
            temp[index] = nums[left]
            index += 1
            left += 1
        while right <= end:
            temp[index] = nums[right]
            index += 1
            right += 1

        for i in range(start, end + 1):
            nums[i] = temp[i]
