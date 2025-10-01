class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for op in operations:
            if op == 'C':
                st.pop()
            elif op == 'D':
                st.append(2 * st[-1])
            elif op == '+':
                st.append(st[-1] + st[-2])
            else:
                st.append(int(op))
        return sum(st)
