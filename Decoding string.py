class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        curr = ""

        for i in s:
            if i.isdigit():
                num = num*10+int(i)

            elif i =='[':
                stack.append((curr,num))
                num = 0
                curr = ""
            elif i == ']':
                prev,repeat = stack.pop()
                curr = prev + curr*repeat
            else:
                curr+=i
        return curr
