class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i , j]

sol = Solution()
[i , j] = sol.twoSum([3,4,5,6] , 9)
print([i , j])
        