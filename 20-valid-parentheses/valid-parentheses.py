class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        closeToOpen = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for ch in s:
            if ch in closeToOpen:
                if not st or st[-1] != closeToOpen[ch]:
                    return False
                st.pop()
            else:
                st.append(ch)
        return len(st) == 0

