class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # rtype = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             rtype.append(nums[i])
        #             rtype.append(nums[j])
        #             break
        # return rtype
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i

if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(nums, target))