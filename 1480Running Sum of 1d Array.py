def runningSum(sums):
    n = len(sums)
    for i in range(n):
        sums[i] = sum(nums[i])
    return(runningSum)


nums = [1,2,3,4]
print(runningSum(nums))