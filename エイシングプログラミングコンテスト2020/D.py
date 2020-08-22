N = int(input())
X = int(input())

def popcount(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

