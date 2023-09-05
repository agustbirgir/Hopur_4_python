k = int(input())#talan
n = int(input())#fjoldi talna 

series_sum = 0#summið

for _ in range(n):
    xi = int(input())
    series_sum += k ** xi

print(series_sum)
