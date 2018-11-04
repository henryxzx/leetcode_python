class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for i in range(len(J)):
            for j in range(len(S)):
                if S[j] == J[i]:
                    count += 1
        return count

if __name__ == '__main__':
    s = Solution()
    J = "aA"
    S = "aAAbbbb"
    print(s.numJewelsInStones(J, S))