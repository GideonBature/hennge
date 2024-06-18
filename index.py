#!/usr/bin/env python3
#######################################################################
# Mission Description
#
# We want you to calculate a sum of squares of given integers, excluding any negatives.
# * The first line of the input will be an integer N (1 <= N <= 100)
# * Each of the test cases will consists of a line with an integer X (0 < X <= 100),
#   followed by another line consisting of X number of space-seperated integers Yn (-100 <= Yn <= 100).
# * For each test case, calculate the sum of squares of the integers excluding any negatives,
#   and print the calculated sum in the output.
# * Note 1: There should be no output until all the input has been received.
# * Note 2: Do not put blank lines between test cases solutions.
# * Note 3: Take input from standard input, and output to standard output.
# 
# ##Rules
# * Choose your favorite language from either of these two: Go, Python
# * Do not use any for loop, while loop, or any list/set/dictionary comprehension
# * Your solution will be tested against Python 3.12 (as of April 2024) or higher
# * def main():
#   ...
#
# * if name === "main":
#       main()
#
# ## Sample Input
# 2
# 4
# 3 -1 1 14
# 5
# 9 6 -53 32 16
#
# ##Sample Output
# 206
# 1397
#######################################################################

import sys

# map function
square_map = lambda x : x*x
sum_map = lambda x: x

# filter function
pos_filter = lambda x: x>0

def get_iteration_times():
    """get the iteration times of input cases: N
    N is in the range: 1 <= N <= 100
    """
    try:
        n = int(input())
        if n <= 0 or n > 100:
            sys.stderr.write("iteration times N (1 <= N <= 100)\n")
            sys.exit(1);
    except ValueError:
        sys.stderr.write("First input should be a integer N, that 1<= N <=100\n")
        sys.exit(1)
    return n

def get_data():
    """parse standard input, first get a integer X(0 < X <= 100)
    then followed by X integers Yn(-100 <= Yn <= 100) space-separated on next line
    """
    try:
        X = int(input())
        if X <= 0 or X > 100:
            sys.stdin.readline() # dump the rest data
            raise ValueError
        Y = map(int, sys.stdin.readline().split())
    except ValueError:
        sys.stderr.write("Input Data Error: ")
        raise ValueError
    return Y

def calculate(times, map_func = sum_map, filter_fun = pos_filter):
    """get data, and calculate a
    """
    if times == 0:
        return 0
    try:
        result = sum(map(map_func, filter(filter_fun, get_data())))
        print(result)
    except ValueError:
        sys.stderr.write("at %d input dataset\n" % (times))
    return calculate(times-1, map_func, filter_fun)


def main():
    n = get_iteration_times()
    calculate(n, square_map, pos_filter)
    

if __name__ == "__main__":
    main()
