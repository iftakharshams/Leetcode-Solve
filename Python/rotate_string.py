class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # Check if lengths are equal and if goal is a substring of s + s
        return len(s) == len(goal) and goal in s + s