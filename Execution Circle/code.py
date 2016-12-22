import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, s = [int(i) for i in input().split()]
d = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# Theory: https://www.youtube.com/watch?v=uCsD3ZGzMgE
# This is known as 'The Josephus Problem'.
# Check wiki: https://en.wikipedia.org/wiki/Josephus_problem#Solution.


# If number of ppl (n) can be represented as 2^a+L
# then the survivor will be at 2L+1. So all we need to find is L.

# To find the max 2^a for any number (n) change the number
# into binary, keep the most significant bit and zero other bits.

# For example for n=13, 2^a = 8
# Binary of 13 = 1101 and if we keep MSB then = 1000
# Decimal of 1000 = 8
# 13 - 8 = 5 = L
# 2L+1 = 11

# now if we start from 5 (s) and go LEFT survivor will be 2
# ((5 + 11) - 1)) % 13 = 2 [you have to substract one considering zero]
# ((s + 2L+1) - 1)) % n  : for left
# ((s - 2L+1) - 1)) % n  : for right

direction = 1 if d == 'LEFT' else -1
survivor = (s + direction * 2 * (n - math.pow(2,len(bin(n)[2:]) - 1))) % n
print(int(survivor))
