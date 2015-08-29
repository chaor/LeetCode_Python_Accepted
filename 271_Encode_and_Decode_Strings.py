# 2015-08-29  Runtime: 148 ms
class Codec:
    # thanks to https://leetcode.com/discuss/54910/1-liners-ruby-python
    # need to use delimiter and make sure this delimiter won't appear in strs
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return ''.join(s.replace('@', '@@') + '$@$' for s in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        return [str.replace('@@', '@') for str in s.split('$@$')[:-1]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))