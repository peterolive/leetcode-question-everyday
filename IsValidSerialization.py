class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # 这种解法是node的数目要比#的数目减1
        preorder = preorder.split(',')
        counter = 1
        for num in preorder:
            if counter == 0:
                return False

            if num != '#':
                counter += 1
            else:
                counter -= 1
            print('num:', num, 'counter:', counter)
        return counter == 0
