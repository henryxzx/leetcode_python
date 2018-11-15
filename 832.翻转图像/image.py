class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # for i in A:
        #     for j in range(int(len(i) / 2)):
        #         i[j], i[-j - 1] = i[-j - 1], i[j]
        #
        # for i in A:
        #     for j in range(len(i)):
        #         if i[j] == 0:
        #             i[j] = 1
        #         else:
        #             i[j] = 0
        # return A
        #一行解法
        return [[j ^ 1 for j in i[::-1]] for i in A]


if __name__ == '__main__':
    a = Solution()
    A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print(a.flipAndInvertImage(A))
