def par(nums):
    new = str(nums)
    new_ = new[::-1]
    if new == new_:
        return True
        
        
nums = 1234321
print(par(nums))