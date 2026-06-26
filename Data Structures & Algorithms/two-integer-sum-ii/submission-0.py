class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l < r:
            while l < r-1 and numbers[l+1] == numbers[l]:
                l+=1
            while l+1 < r and numbers[r-1] == numbers[r]:
                r-=1 
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1, r+1]
            elif sum < target:
                l+=1
            else:
                r-=1
        
            
        