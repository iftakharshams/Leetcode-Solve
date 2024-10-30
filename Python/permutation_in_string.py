from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Base condition
        if len(s1) > len(s2):
            return False
        
        # Frequency count of s1
        s1_count = Counter(s1)
        # Initial window in s2 with the same length as s1
        s2_count = Counter(s2[:len(s1)])
        
        # Slide the window over s2
        for i in range(len(s1), len(s2)):
            # Check if counts match
            if s1_count == s2_count:
                return True
            
            # Update the window: add new char and remove the old char
            start_char = s2[i - len(s1)]
            end_char = s2[i]
            
            s2_count[end_char] += 1
            s2_count[start_char] -= 1
            
            # Remove the count if it becomes zero for clean comparison
            if s2_count[start_char] == 0:
                del s2_count[start_char]
        
        # Check the last window after the loop
        return s1_count == s2_count