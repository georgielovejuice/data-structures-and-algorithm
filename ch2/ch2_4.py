def threeSum(nums):
    nums.sort()  
    result = []
    if len(nums) < 3:
        return "Array Input Length Must More Than 2" 
    else:    
        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i-1]:  
                continue
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
            
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1  # We need a larger number
                else:
                    right -= 1  # We need a smaller number
        
        return result


nums_list = [int(num) for num in input("Enter Your List : ").split()]
result = threeSum(nums_list)
print(result)

