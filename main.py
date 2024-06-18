def main():
    N = int(input())
    for _ in range(N):
        X = int(input())
        Y = list(map(int, input().split()))
        sum_of_squares = sum(i**2 for i in Y if i >= 0)
        print(sum_of_squares)

if __name__ == "__main__":
    main()
