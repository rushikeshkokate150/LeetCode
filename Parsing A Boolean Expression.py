class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for ch in expression:

            if ch != ')':
                stack.append(ch)
            else:
                ar = []
                j = stack.pop()

                while j != '(':
                    if j == 't':
                        ar.append(True)
                    elif j == 'f':
                        ar.append(False)

                    j = stack.pop()

                op = stack.pop()

                if op == '&':
                    val = all(ar)

                elif op == '|':
                    val = any(ar)

                else:
                    val = not ar[0]
                stack.append('t' if val else 'f')

        return stack[-1] == 't'