amount = int(input())

for p in range(amount):
    x = int(input())
    nums = [int(i) for i in input().split(" ")]
    # Checks for list of 0 to avoid dividing by 0 also gets highest value
    low = min(nums)
    high = max(nums)
    if low == high:
        print(0)
        continue
    # Gets Total value of all nums
    total = 0
    for i in nums:
        total += i
    # Gets possible divisors of the total
    possible_divisors = []
    for i in range(high, total + 1):
        if total % i == 0:
            possible_divisors.append(i)
    # Loops through divisors + nums to find correct divisor
    for a in possible_divisors:
        count = 0
        target = total // a
        totals = 0
        for b in nums:
            totals += b
            if totals == int(a):
                count += 1
                totals = 0
            if count == target:
                divisor = a
                break
        else:
            continue
        break   
    print(x - target)
