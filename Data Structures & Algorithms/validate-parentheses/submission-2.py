class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "]" or c == "}" or c == ")":
                if len(stack) == 0:
                    return False
                else:
                    if c == "]" and stack[-1] != "[":
                        return False
                    elif c == "}" and stack[-1] != "{":
                        return False
                    elif c == ")" and stack[-1] != "(":
                        return False
                    else:
                        stack.pop()
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        return False