class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            integer = digits[0]
            for i in range(1, len(digits)):
                integer = integer*10 + digits[i]
            integer += 1
            return list(str(integer))