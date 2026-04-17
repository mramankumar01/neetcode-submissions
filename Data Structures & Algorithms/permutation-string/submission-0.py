class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        countS1 = [0] * 26
        countW = [0] * 26
        for c in s1:
            countS1[ord(c) - ord('a')] += 1
        # initialize first window
        for i in range(len(s1)):
            countW[ord(s2[i]) - ord('a')] += 1
        matches = sum(1 for i in range(26) if countS1[i] == countW[i])
        # slide window
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            # add new right character
            idx = ord(s2[r]) - ord('a')
            countW[idx] += 1
            if countW[idx] == countS1[idx]: matches += 1
            elif countW[idx] - 1 == countS1[idx]: matches -= 1
            # Reomove old left character
            idx = ord(s2[r - len(s1)]) - ord('a')
            countW[idx] -= 1
            if countW[idx] == countS1[idx]: matches += 1
            elif countW[idx] + 1 == countS1[idx]: matches -= 1
        return matches == 26