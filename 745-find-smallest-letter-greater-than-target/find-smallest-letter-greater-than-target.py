
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        low = 0
        high = len(letters) - 1
        ans = letters[0]   # default wrap-around answer
        
        while low <= high:
            mid = (low + high) // 2
            
            if letters[mid] > target:
                ans = letters[mid]   # possible answer
                high = mid - 1       # search left
            else:
                low = mid + 1        # search right
                
        return ans

        

        