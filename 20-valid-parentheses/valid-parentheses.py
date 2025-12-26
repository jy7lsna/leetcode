class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or stack[-1] != closedToOpen[ch]:
                    return False
                stack.pop()
        return len(stack) == 0