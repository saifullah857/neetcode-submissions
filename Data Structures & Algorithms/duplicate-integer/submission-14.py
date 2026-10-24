class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
                
        for key, value in seen.items():
            if value > 1:
                return True
                
        return False