class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        stack = []
        
        for char in expression:
            if char == ',':
                # Ignore commas as they are just separators
                continue
            elif char in 'tf':
                # Push True for 't' and False for 'f'
                stack.append(char == 't')
            elif char in '(&|!':
                # Push operators to the stack
                stack.append(char)
            elif char == ')':
                # Evaluate the expression inside the parentheses
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()  # Remove the '('
                operator = stack.pop()
                
                if operator == '&':
                    stack.append(all(temp))
                elif operator == '|':
                    stack.append(any(temp))
                elif operator == '!':
                    stack.append(not temp[0])
            else:
                # Push open parentheses
                stack.append(char)
        
        # The result will be the only element left in the stack
        return stack[0]
