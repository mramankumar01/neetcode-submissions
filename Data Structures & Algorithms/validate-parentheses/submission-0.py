class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = deque()
        for c in s:
            if c in '([{':
                stack.append(c)
            elif c in ')]}':
                pair = pairs[c]
                if (not stack) or pair != stack.pop():
                    return False
        
        return len(stack) == 0