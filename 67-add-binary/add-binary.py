class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1 = int(a, 2)
        num2 = int(b, 2)
        
        # Add them
        total = num1 + num2
        
        # Convert back to binary string (remove '0b' prefix)
        return bin(total)[2:]