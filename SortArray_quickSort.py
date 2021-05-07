from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, start, end):
        if start >= end:
            return
        left, right = start, end
        mid = start + (end - start) // 2
        pivot = nums[mid]

        while left <= right:
            while left <= right and nums[left] < pivot:  # 如果 <= pivot的话有可能会略过pivot
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quick_sort(nums, start, left)
        self.quick_sort(nums, right, end)
