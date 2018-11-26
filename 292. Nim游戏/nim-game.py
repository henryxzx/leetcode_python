class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 巴什博弈
        if n % 4 == 0:
            return False
        else:
            return True


