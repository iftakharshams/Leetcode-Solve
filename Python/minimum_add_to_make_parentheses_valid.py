class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Count of open parentheses that are unmatched
        open_count = 0
        # Count of unmatched closing parentheses
        close_count = 0

        # Iterate through the string
        for char in s:
            if char == '(':
                # Increment open_count for an open parenthesis
                open_count += 1
            elif char == ')':
                if open_count > 0:
                    # Match a closing parenthesis with an open parenthesis
                    open_count -= 1
                else:
                    # Increment close_count if there's no matching open parenthesis
                    close_count += 1

        # The total number of unmatched parentheses is the sum of open_count and close_count
        return open_count + close_count

# Example usage
solution = Solution()
print(solution.minAddToMakeValid("())"))
print(solution.minAddToMakeValid("(((")) 
