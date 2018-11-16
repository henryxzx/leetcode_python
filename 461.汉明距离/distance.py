class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # count = 0
        # for i in bin(x ^ y).replace('0b', ''):
        #     if i == '1':
        #         count = count + 1
        # return count
        return len([i for i in bin(x ^ y).replace('0b', '') if i == '1'])


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1, 4))