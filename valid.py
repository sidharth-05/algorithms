class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for paren in s:
            if len(stack) == 0:
                stack.append(paren)
            elif paren == "{":
                stack.append(paren)
            elif paren == "[":
                stack.append(paren)
            elif paren == "(":
                stack.append(paren)
            elif paren == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif paren == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif paren == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0