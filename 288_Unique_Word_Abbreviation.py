# 2016-01-02  53 tests, 168 ms
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.d = {}
        for word in dictionary:
            abbr = word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]
            self.d[abbr] = word if abbr not in self.d else '' if self.d[abbr] != word else self.d[abbr]

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]
        return abbr not in self.d or self.d[abbr] == word

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
