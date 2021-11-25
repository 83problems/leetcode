start_parens = [ '{', '(', '[' ]
parens_map = { '}': '{', ')': '(', ']': '[' }

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in start_parens:
                stack.append(i)
            elif not stack:
                return False
            elif stack.pop() != parens_map[i]:
                return False 
        return not stack