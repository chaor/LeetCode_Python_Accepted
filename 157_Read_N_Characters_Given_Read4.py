# 2015-05-11  Runtime: 50 ms

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        buffer, readBytes, endOfFile = [None, None, None, None], 0, False
        while not endOfFile and readBytes < n:
            sz = read4(buffer)
            if sz < 4: endOfFile = True
            bytes = min(n - readBytes, sz)
            for i in xrange(bytes): buf[readBytes + i] = buffer[i]
            readBytes += bytes
        return readBytes