class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for chr in s:
            if chr.isalnum():
                clean += chr.lower()
        return clean == clean[::-1]

sol = Solution()
status = sol.isPalindrome("Was it a car or a cat I saw?")
print(status)

        