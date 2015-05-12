# 2015-05-11  Runtime: 60 ms

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    
    def __init__(self):
        self.buffer, self.offset, self.bufsize = [None, None, None, None], 0, 0
    
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        readBytes, endOfFile = 0, False
        while not endOfFile and readBytes < n:
            if self.bufsize == 0:
                self.bufsize = read4(self.buffer)
                endOfFile = self.bufsize < 4
            bytes = min(n - readBytes, self.bufsize)
            for i in xrange(bytes): buf[readBytes + i] = self.buffer[self.offset + i]
            self.offset = (self.offset + bytes) % 4
            self.bufsize -= bytes
            readBytes += bytes
        return readBytes