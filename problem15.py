# Move right 20 times and down 20 times
# Number of routes is arrangements of 'r'*20 + 'd'*20
# 40!/(20! 20!)

from common import prod

print prod(range(21, 41))/prod(range(1,21))