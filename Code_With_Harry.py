nums = set()

x = input('What numbers you choose: ')

fok = x.split(' ')

for fish in fok:
    nums.add(int(fish))

for charm in nums:
    print(charm)