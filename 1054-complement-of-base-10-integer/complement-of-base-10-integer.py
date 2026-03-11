class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        
        b = bin(n)[2:]
        flipped = ""
        
        for bit in b:
            if bit == '0':
                flipped += '1'
            else:
                flipped += '0'
        
        return int(flipped, 2)