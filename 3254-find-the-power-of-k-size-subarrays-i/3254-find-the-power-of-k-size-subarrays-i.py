from typing import List

class Solution:
    def _check_consecutive(self, nums: List[int], start: int, length: int) -> int:
        """
        Helper function to check if elements from 'start' to 'start + length - 1' are consecutive.
        """
        for i in range(start + 1, start + length):
            if nums[i] - nums[i - 1] != 1:
                return -1
        return nums[start + length - 1]

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        """
        Main function to return a list where each element is the result of applying '_check_consecutive'
        on each subarray of length 'k'.
        """
        n = len(nums)
        result = []
        
        for i in range(n - k + 1):
            result.append(self._check_consecutive(nums, i, k))
        
        return result
