def unique(nums):
    result=0
    for num in nums:
        result=result^num

    return result


nums=[4,2,2,1,3,3,1]

print(unique(nums))