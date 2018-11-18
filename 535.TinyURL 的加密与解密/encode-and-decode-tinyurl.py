class Codec:
    def __init__(self):
        self.dict = {}
        self.key = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        import uuid
        self.key = uuid.uuid4()
        txt = 'http://tinyurl.com/' + str(self.key)
        self.dict[txt] = longUrl
        return txt

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.dict[shortUrl]


# Your Codec object will be instantiated and called as such:
codec = Codec()
url = 'https://leetcode.com/problems/design-tinyurl'
print(codec.encode(url))
print(codec.decode(codec.encode(url)))