class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {')' : '(', ']' : '[', '}' : '{'}
        for parenthesis in s:
            if parenthesis in "([{":
                stack.append(parenthesis)
            else:
                if len(stack) == 0 or stack[-1] != close_to_open[parenthesis]:
                    return False
                stack.pop()
        return len(stack) == 0


            