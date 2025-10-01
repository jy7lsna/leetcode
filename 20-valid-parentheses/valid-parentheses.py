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
                if st and st[-1] == closeToOpen[ch]:
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)
        return len(st) == 0

