class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        U, D, L, R = 0, 0, 0, 0
        for i in moves:
            if i == 'U':
                U += 1
            elif i == 'D':
                D += 1
            elif i == 'L':
                L += 1
            elif i == 'R':
                R += 1
            else:
                return False
        if U == D and L == R:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    moves = 'LL'
    print(s.judgeCircle(moves))