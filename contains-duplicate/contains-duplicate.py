class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        self.nums = nums
        if len(nums) > len(set(nums)):
            return True
        else:
            return False
