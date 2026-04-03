class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ''
        for ch in s:
            if ch.isalnum():
                ns += ch.lower()
        return ns == ns[::-1]