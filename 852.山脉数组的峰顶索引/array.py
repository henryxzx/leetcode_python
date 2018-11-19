class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max = 0
        index = 0
        for i in range(len(A)):
            if A[i] > max:
                max = A[i]
                index = i
        return index


if __name__ == '__main__':
    a = Solution()
    print(a.peakIndexInMountainArray([0, 1, 2, 0]))