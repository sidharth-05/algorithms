N = input()

MAXIMUM = 0
CURRENT = 0

for num in int(N):
    if num == '1':
        CURRENT = CURRENT + 1
    else:
        MAXIMUM = max(MAXIMUM, CURRENT)
        CURRENT = 0

print(max(MAXIMUM, CURRENT))

# TasK : Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation. When working with different bases, it is common to show the base as a subscript.