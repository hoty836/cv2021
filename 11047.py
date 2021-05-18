
n, k = map(int, input().split())

data = []
result = 0

for _ in range(n):
    a = int(input())
    data.append(a)


for i in range(n):
    if data[i]>=k : break

for j in range(i, -1, -1):
    result += k // data[j]
    k %= data[j]

print(result)

