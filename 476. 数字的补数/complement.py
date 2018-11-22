class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while num >= i:
            # num每次与i做亦或运算
            num ^= i
            # i每次左移一位，即乘2
            i <<= 1
        return num


if __name__ == '__main__':
    a = Solution()
    print(a.findComplement(5))

