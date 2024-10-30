from heapq import heappush, heappop
import sys

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # Initialize the min-heap and find the initial max value
        min_heap = []
        current_max = -sys.maxsize
        for i in range(len(nums)):
            heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])
        
        # Initialize the smallest range as [smallest number, largest number]
        smallest_range = [-sys.maxsize, sys.maxsize]
        
        while min_heap:
            current_min, list_idx, element_idx = heappop(min_heap)
            
            # Check if the current range is smaller
            if current_max - current_min < smallest_range[1] - smallest_range[0]:
                smallest_range = [current_min, current_max]
            
            # Move to the next element in the list
            if element_idx + 1 < len(nums[list_idx]):
                next_value = nums[list_idx][element_idx + 1]
                heappush(min_heap, (next_value, list_idx, element_idx + 1))
                # Update the current max if the new value is greater
                current_max = max(current_max, next_value)
            else:
                # If any list is exhausted, break
                break
        
        return smallest_range
