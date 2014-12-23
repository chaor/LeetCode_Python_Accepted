# 2014-12-18  Runtime: 148 ms
class Solution:
    # @return a string
    def fractionToDecimal(self, n, d):
        res = []
        if (n > 0 and d < 0) or (n < 0 and d > 0): res.append('-')
        n, d = abs(n), abs(d)
        
        # integral part, 整数部分
        res.append(str(n/d))
        
        remainder = n % d
        if remainder == 0: return ''.join(res) # list to string
        
        res.append('.')
        # key is remainder, value is the position of str(remainder * 10 / d) in list "res"
        # In this way we know where to add '(' , ')'
        # 需要一个字典，键是余数，值是(此余数 * 10 / d)的字符串形式在res列表的位置
        # 这样我们就知道在哪里插入'('和')'了
        remainderPos = {}
        while remainder > 0:
            if remainder in remainderPos:
                res.insert(remainderPos[remainder], '(')
                res.append(')')
                return ''.join(res) # list to string
            remainderPos[remainder] = len(res) 
            res.append(str(remainder * 10 / d))
            remainder = remainder * 10 % d
        return ''.join(res) # list to string