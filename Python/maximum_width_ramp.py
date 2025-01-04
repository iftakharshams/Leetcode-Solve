class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Create a list of (value, index) pairs and sort by value, then by index
        sorted_nums = sorted((num, i) for i, num in enumerate(nums))
        
        max_width = 0
        min_index = float('inf')

        # Iterate through the sorted list to find the maximum width ramp
        for _, index in sorted_nums:
            max_width = max(max_width, index - min_index)
            min_index = min(min_index, index)
        
        return max_width
