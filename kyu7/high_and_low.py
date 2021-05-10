def high_and_low(numbers):
    high = (sorted([int(i) for i in numbers.split()])[-1])
    low = sorted([int(i) for i in numbers.split()])[0]
    
    return str(high)+ " " + str (low) 

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))


# More clever solution

def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])