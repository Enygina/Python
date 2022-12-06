#В файле находится N натуральных чисел,
# записанных через пробел. Среди чисел не
# хватает одного, чтобы выполнялось условие
# A[i] - 1 = A[i-1]. Найдите это число.

with open('s5t2.txt', 'r') as f:
    nums = list(map(int, f.read().split()))
print(nums)
for i in range(1,len(nums)):
    if (nums[i]-nums[i-1])>1:
        nums.insert(i, nums[i-1]+1)
print(nums)

with open('s5t2.txt', 'w') as f:
    f.write(" ".join(list(map(str, nums))))