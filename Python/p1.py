r, c = map(int, input("Enter rows and columns: ").split())
a = []
print("Enter elements:")
for i in range(r):
    row = list(map(int, input().split()))
    a.append(row)

print("Rotated matrix:")
for j in range(c):
    for i in range(r-1, -1, -1):
        print(a[i][j], end=' ')
    print()
