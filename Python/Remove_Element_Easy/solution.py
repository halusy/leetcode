class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        temp = []
        for each in nums:
            if each != val:
                k = k + 1
                temp.insert(0, each)
        print(temp)
        nums[:] = temp
        return k