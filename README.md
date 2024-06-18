#######################################################################
# Mission Description

We want you to calculate a sum of squares of given integers, excluding any negatives.

## Input

1. The first line of the input will be an integer N (1 <= N <= 100).
2. Each of the test cases will consist of a line with an integer X (0 < X <= 100), followed by another line consisting of X number of space-separated integers Yn (-100 <= Yn <= 100).

## Output

For each test case, calculate the sum of squares of the integers excluding any negatives, and print the calculated sum in the output.

### Notes:
1. There should be no output until all the input has been received.
2. Do not put blank lines between test case solutions.
3. Take input from standard input, and output to standard output.

## Rules

1. Choose your favorite language from either of these two: Go, Python.
2. Do not use any `for` loop, `while` loop, or any list/set/dictionary comprehension.
3. Your solution will be tested against Python 3.12 (as of April 2024) or higher.
4. Code must include a main() function:

    ```python
    def main():
        ...
    
    if __name__ == "__main__":
        main()
    ```

## Sample Input
    2
    4
    3 -1 1 14
    5
    9 6 -53 32 16

## Sample Output
    206
    1397

#######################################################################
