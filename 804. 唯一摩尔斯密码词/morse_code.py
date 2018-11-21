class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        str_morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        str_words = 'abcdefghijklmnopqrstuvwxyz'
        count = set()
        for i in range(len(words)):
            str_target = ''
            for j in range(len(words[i])):
                str_target += str_morse[str_words.index(words[i][j])]
            count.add(str_target)

        return len(count)

if __name__ == '__main__':
    s = Solution()
    words = ["gin", "zen", "gig", "msg"]
    print(s.uniqueMorseRepresentations(words))
