class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if stack[-1] < -a:
                    stack.pop()
                elif stack[-1] > -a:
                    a = 0
                else:
                    stack.pop()
                    a = 0
            if a:  # a != 0
                stack.append(a)
        return stack