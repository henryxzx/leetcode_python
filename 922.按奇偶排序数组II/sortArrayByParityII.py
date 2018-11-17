class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even, odd, ans = [], [], []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(len(A)):
            if i % 2 == 0:
                ans.append(even.pop())
            else:
                ans.append(odd.pop())
