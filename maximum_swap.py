class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = list(str(num))
        last = {int(d): i for i, d in enumerate(num_str)}
        
        for i, d in enumerate(num_str):
            for x in range(9, int(d), -1):  # Check for larger digits
                if last.get(x, -1) > i:  # If a larger digit exists later
                    # Swap the digits
                    num_str[i], num_str[last[x]] = num_str[last[x]], num_str[i]
                    return int(''.join(num_str))  # Return the new number
        return num  # No swap made, return original number
