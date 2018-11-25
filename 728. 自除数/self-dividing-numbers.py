class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        rList = []
        for i in range(left, right + 1):
            num = i
            while num > 0:
                if num % 10 == 0:
                    break
                elif i % (num % 10) == 0:
                    num = num // 10
                else:
                    break
            else:
                rList.append(i)
        return rList


if __name__ == '__main__':
    a = Solution()
    print(a.selfDividingNumbers(1, 22))