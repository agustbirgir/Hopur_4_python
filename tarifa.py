mb_per_month = int(input())
n = int(input())
eftir = 0
for x in range(n):
    mb_this_month = int(input())
    left = mb_per_month - mb_this_month
    eftir += left
print(eftir+mb_per_month)