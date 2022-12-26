nums = []
last = input()
while last != '':
    nums.append(int(last))
    last = input()
nums = [n * 811589153 for n in nums] #get rid of this line for part 1

indices = [i for i in range(len(nums))]
for t in range(10): #and this outer for loop too
    for i in range(len(indices)):
        idx = indices.index(i)
        indices.remove(i)
        indices.insert((idx + nums[i]) % len(indices), i)

zero_idx = indices.index(nums.index(0))
a = nums[indices[(zero_idx + 1000) % len(indices)]]
b = nums[indices[(zero_idx + 2000) % len(indices)]]
c = nums[indices[(zero_idx + 3000) % len(indices)]]
print(a + b + c)
