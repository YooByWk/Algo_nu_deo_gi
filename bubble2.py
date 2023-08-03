def bubble2(nums):
    n = len(nums)
    for phase in range(0, n-1):
        for j in range(phase):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1], nums[j]
    return

aaaa = [55, 7, 78, 12, 42]
bubble2(aaaa)
print(aaaa)