class Solution(object):
    def removeDuplicates(self, nums):
        i = 0 
        while i < len(nums):
            j = i + 1
            token = False
            while j < len(nums):
                if nums[i] == nums[j]:
                    nums.pop(i)
                    token = True
                j = j + 1
            if token == False:
                i = i + 1
