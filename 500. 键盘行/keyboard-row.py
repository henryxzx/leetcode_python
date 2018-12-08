class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1, set2, set3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        res = []
        for word in words:
            s = set(word.lower())
            if s.issubset(set1) or s.issubset(set2) or s.issubset(set3):
                res.append(word)

        return res


if __name__ == '__main__':
    s = Solution()
    case = ["Hello", "Alaska", "Dad", "Peace"]
    print(s.findWords(case))
