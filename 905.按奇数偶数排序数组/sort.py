class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        oushu = []
        jishu = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                oushu.append(A[i])
            else:
                jishu.append(A[i])
        oushu.extend(jishu)
        return oushu

if __name__ == '__main__':
    s = Solution()
    a = [3, 1, 2, 4]
    print(s.sortArrayByParity(a))