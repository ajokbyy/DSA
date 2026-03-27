class Solution(object):
    def areSimilar(self, mat, k):
        m, n = len(mat), len(mat[0])
        k = k % n
        
        for i in range(m):
            if i % 2 == 0:
                # left shift check
                if mat[i] != mat[i][k:] + mat[i][:k]:
                    return False
            else:
                # right shift check
                if mat[i] != mat[i][-k:] + mat[i][:-k]:
                    return False
        
        return True