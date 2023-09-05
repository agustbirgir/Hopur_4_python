first = int(input())
second = int(input())

if first < 0 or second < 0 or first > 10**6 or second > 10**6:
    print("Input values are out of the valid range.")

else:
    result = 0
    for _ in range(second):
        result += first

    print(result)
